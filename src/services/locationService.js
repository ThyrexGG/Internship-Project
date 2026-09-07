/**
 * HomeSweet Location & Reverse Geocoding Service
 * Context-aware geolocation with graceful degradation and offline district mapping.
 */

// Reference coordinate centers for Phnom Penh districts
const DISTRICT_CENTERS = [
  { name: 'Chroy Chongva', lat: 11.5900, lng: 104.9300 },
  { name: 'BKK1', lat: 11.5500, lng: 104.9250 },
  { name: 'Tonle Bassac', lat: 11.5450, lng: 104.9350 },
  { name: 'Sen Sok', lat: 11.5750, lng: 104.8850 },
  { name: 'Toul Kork', lat: 11.5700, lng: 104.9000 },
  { name: 'Chamkarmon', lat: 11.5400, lng: 104.9200 },
  { name: 'Daun Penh', lat: 11.5650, lng: 104.9250 }
]

function getNearestDistrict(lat, lng) {
  let nearest = DISTRICT_CENTERS[0]
  let minDistance = Infinity

  DISTRICT_CENTERS.forEach(d => {
    const dist = Math.hypot(d.lat - lat, d.lng - lng)
    if (dist < minDistance) {
      minDistance = dist
      nearest = d
    }
  })
  return nearest.name
}

/**
 * Request device location with explicit user action
 */
export function getCurrentCoordinates(options = {}) {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      return reject(new Error('Geolocation is not supported by your browser.'))
    }

    const defaultOptions = {
      enableHighAccuracy: true,
      timeout: 10000,
      maximumAge: 60000,
      ...options
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        resolve({
          lat: position.coords.latitude,
          lng: position.coords.longitude,
          accuracy: position.coords.accuracy
        })
      },
      (error) => {
        let message = 'Unable to retrieve location.'
        switch (error.code) {
          case error.PERMISSION_DENIED:
            message = 'Location permission was denied. Please enter address manually.'
            break
          case error.POSITION_UNAVAILABLE:
            message = 'Location information is currently unavailable.'
            break
          case error.TIMEOUT:
            message = 'Location request timed out. Please try again or type manually.'
            break
        }
        reject(new Error(message))
      },
      defaultOptions
    )
  })
}

/**
 * Convert latitude and longitude to human-readable address string
 */
export async function reverseGeocodeCoordinates(lat, lng) {
  // 1. Try Google Maps Geocoder if loaded in window
  if (window.google?.maps?.Geocoder) {
    try {
      const geocoder = new window.google.maps.Geocoder()
      const response = await new Promise((resolve, reject) => {
        geocoder.geocode({ location: { lat, lng } }, (results, status) => {
          if (status === 'OK' && results && results[0]) {
            resolve(results[0])
          } else {
            reject(new Error('Google Geocoder returned no results.'))
          }
        })
      })

      return {
        formattedAddress: response.formatted_address,
        lat,
        lng,
        source: 'google'
      }
    } catch (gErr) {
      console.warn('Google reverse geocode fallback:', gErr)
    }
  }

  // 2. Try OpenStreetMap Nominatim reverse geocoding
  try {
    const controller = new AbortController()
    const timeoutId = setTimeout(() => controller.abort(), 4000)

    const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&zoom=16&addressdetails=1`
    const res = await fetch(url, {
      signal: controller.signal,
      headers: {
        'Accept-Language': 'en'
      }
    })
    clearTimeout(timeoutId)

    if (res.ok) {
      const data = await res.json()
      if (data && data.display_name) {
        const addr = data.address || {}
        const district = addr.suburb || addr.neighbourhood || addr.city_district || getNearestDistrict(lat, lng)
        const city = addr.city || addr.town || 'Phnom Penh'
        const shortAddr = `${district}, ${city}`

        return {
          formattedAddress: shortAddr,
          fullAddress: data.display_name,
          district,
          city,
          country: addr.country || 'Cambodia',
          lat,
          lng,
          source: 'nominatim'
        }
      }
    }
  } catch (osmErr) {
    console.warn('Nominatim reverse geocode fallback:', osmErr)
  }

  // 3. Resilient offline fallback using nearest known Phnom Penh district
  const fallbackDistrict = getNearestDistrict(lat, lng)
  return {
    formattedAddress: `${fallbackDistrict}, Phnom Penh`,
    district: fallbackDistrict,
    city: 'Phnom Penh',
    country: 'Cambodia',
    lat,
    lng,
    source: 'offline_district'
  }
}
