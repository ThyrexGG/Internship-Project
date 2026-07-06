import { ref } from 'vue'

export const properties = ref([
  {
    id: 1, name: 'Skystar Condo', price: 200, type: 'condo',
    location: 'Chroy Chongva, Phnum Penh', lat: 11.5900, lng: 104.9300,
    beds: 2, baths: 4, sqft: 180, match: 99,
    liked: false, activeSlide: 0,
    rating: 4.9, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'ac', 'pool', 'parking'],
    images: [
      'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=600&q=80',
      'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=600&q=80',
      'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=600&q=80',
    ]
  },
  {
    id: 2, name: 'Aurafa Condo', price: 120, type: 'condo',
    location: 'Chroy Chongva, Phnum Penh', lat: 11.5950, lng: 104.9350,
    beds: 1, baths: 2, sqft: 100, match: 97,
    liked: false, activeSlide: 0,
    rating: 4.7, period: 'Short-term',
    amenities: ['wifi', 'ac', 'washer'],
    images: [
      'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600&q=80',
      'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600&q=80',
      'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=600&q=80',
    ]
  },
  {
    id: 3, name: 'High Dafa', price: 230, type: 'apartment',
    location: 'Chroy Chongva, Phnum Penh', lat: 11.5850, lng: 104.9250,
    beds: 3, baths: 2, sqft: 200, match: 95,
    liked: false, activeSlide: 0,
    rating: 4.5, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'washer', 'ac', 'parking'],
    images: [
      'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&q=80',
      'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=600&q=80',
      'https://images.unsplash.com/photo-1507089947368-19c1da9775ae?w=600&q=80',
    ]
  },
  {
    id: 4, name: 'Phnom Star', price: 175, type: 'apartment',
    location: 'BKK1, Phnum Penh', lat: 11.5500, lng: 104.9250,
    beds: 2, baths: 2, sqft: 130, match: 94,
    liked: false, activeSlide: 0,
    rating: 4.6, period: 'Short-term',
    amenities: ['wifi', 'ac', 'washer', 'parking'],
    images: [
      'https://images.unsplash.com/photo-1600210492493-0946911123ea?w=600&q=80',
      'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80',
      'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80',
    ]
  },
  {
    id: 5, name: 'Mekong View', price: 310, type: 'house',
    location: 'Tonle Bassac, Phnum Penh', lat: 11.5450, lng: 104.9350,
    beds: 3, baths: 3, sqft: 250, match: 92,
    liked: false, activeSlide: 0,
    rating: 4.8, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'washer', 'ac', 'parking', 'pool'],
    images: [
      'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=600&q=80',
      'https://images.unsplash.com/photo-1600566752355-35792bedcfea?w=600&q=80',
      'https://images.unsplash.com/photo-1583608205776-bfd35f0d9f83?w=600&q=80',
    ]
  },
  {
    id: 6, name: 'Lotus Residence', price: 145, type: 'house',
    location: 'Sen Sok, Phnum Penh', lat: 11.5750, lng: 104.8850,
    beds: 1, baths: 1, sqft: 85, match: 91,
    liked: false, activeSlide: 0,
    rating: 4.2, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'ac', 'parking'],
    images: [
      'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=600&q=80',
      'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80',
      'https://images.unsplash.com/photo-1484101403633-562f891dc89a?w=600&q=80',
    ]
  },
  {
    id: 7, name: 'Diamond Tower', price: 400, type: 'condo',
    location: 'Daun Penh, Phnum Penh', lat: 11.5650, lng: 104.9250,
    beds: 4, baths: 3, sqft: 320, match: 90,
    liked: false, activeSlide: 0,
    rating: 4.9, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'washer', 'ac', 'parking', 'pool'],
    images: [
      'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&q=80',
      'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=600&q=80',
      'https://images.unsplash.com/photo-1598928636135-d146006ff4be?w=600&q=80',
    ]
  },
  {
    id: 8, name: 'Green Park Suite', price: 190, type: 'apartment',
    location: 'Toul Kork, Phnum Penh', lat: 11.5700, lng: 104.9000,
    beds: 2, baths: 2, sqft: 155, match: 89,
    liked: false, activeSlide: 0,
    rating: 4.4, period: 'Short-term',
    amenities: ['wifi', 'ac', 'washer', 'parking'],
    images: [
      'https://images.unsplash.com/photo-1560185007-cde436f6a4d0?w=600&q=80',
      'https://images.unsplash.com/photo-1617103996702-96ff29b1c467?w=600&q=80',
      'https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=600&q=80',
    ]
  },
  {
    id: 9, name: 'Royal Terrace', price: 265, type: 'house',
    location: 'Chamkarmon, Phnum Penh', lat: 11.5400, lng: 104.9200,
    beds: 3, baths: 2, sqft: 210, match: 88,
    liked: false, activeSlide: 0,
    rating: 4.7, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'washer', 'ac', 'parking', 'pool'],
    images: [
      'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=80',
      'https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&q=80',
      'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80',
    ]
  },
  {
    id: 10, name: 'Urban Oasis Studio', price: 150, type: 'studio',
    location: 'Toul Kork, Phnum Penh', lat: 11.5720, lng: 104.8950,
    beds: 1, baths: 1, sqft: 65, match: 96,
    liked: false, activeSlide: 0,
    rating: 4.6, period: 'Short-term',
    amenities: ['wifi', 'ac', 'kitchen'],
    images: [
      'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=600&q=80',
      'https://images.unsplash.com/photo-1502672023488-70e25813eb80?w=600&q=80',
    ]
  },
  {
    id: 11, name: 'Skyline Premium Penthouse', price: 550, type: 'condo',
    location: 'BKK1, Phnum Penh', lat: 11.5520, lng: 104.9280,
    beds: 4, baths: 3, sqft: 310, match: 98,
    liked: false, activeSlide: 0,
    rating: 5.0, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'washer', 'ac', 'parking', 'pool'],
    images: [
      'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600&q=80',
      'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80',
    ]
  },
  {
    id: 12, name: 'Green Village Residence', price: 280, type: 'house',
    location: 'Sen Sok, Phnum Penh', lat: 11.5760, lng: 104.8870,
    beds: 3, baths: 2, sqft: 195, match: 93,
    liked: false, activeSlide: 0,
    rating: 4.8, period: 'Long-term',
    amenities: ['wifi', 'kitchen', 'ac', 'parking'],
    images: [
      'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80',
      'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600&q=80',
    ]
  },
])

export const globalSearchQuery = ref('')
export const globalFilterState = ref({
  type: 'Any type',
  priceMin: 50,
  priceMax: 610,
  bedrooms: 0,
  beds: 0,
  bathrooms: 0,
  amenities: [],
  rate: 'Any',
  period: 'Any'
})

