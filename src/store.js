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
      '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg',
      '/homesweet/b389fd58-2a76-4d56-8190-cb65043ffea1.jpeg',
      '/homesweet/cab57881-edf1-4915-a22b-a68cf4ebc688.jpeg',
      '/homesweet/62e59b68-a0b1-43bd-96e1-04a698571889.jpeg',
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
      '/homesweet/86af45b4-efa9-4714-84bb-c02232f793cc.jpeg',
      '/homesweet/Gemini_Generated_Image_iia6ltiia6ltiia6.jpeg',
      '/homesweet/34480425-676e-4c64-9f85-ae9c934c5312.jpeg',
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
      '/homesweet/2baa9b76-ed0e-4bbe-b781-1c26656a2de1.jpeg',
      '/homesweet/f84a3f68-132e-455c-be67-2c58bf65c082.jpeg',
      '/homesweet/72ea68a6-2723-46a8-b29e-c60724e0e849.jpeg',
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
      '/homesweet/Gemini_Generated_Image_551nik551nik551n.jpeg',
      '/homesweet/a492688d-f4de-4d9f-9077-0a0ba52fc44e.jpeg',
      '/homesweet/62e59b68-a0b1-43bd-96e1-04a698571889.jpeg',
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
      '/homesweet/Gemini_Generated_Image_4slxg94slxg94slx.jpeg',
      '/homesweet/b389fd58-2a76-4d56-8190-cb65043ffea1.jpeg',
      '/homesweet/465fdd21-b72c-4512-875f-ea562b99a5c1.jpeg',
      '/homesweet/740dbb11-17eb-4bf2-a6ef-eb5056550dbe.jpeg',
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
      '/homesweet/Gemini_Generated_Image_nwqd1nwqd1nwqd1n.jpeg',
      '/homesweet/Gemini_Generated_Image_iia6ltiia6ltiia6.jpeg',
      '/homesweet/a492688d-f4de-4d9f-9077-0a0ba52fc44e.jpeg',
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
      '/homesweet/cc362a63-5a5e-4f09-8722-cb6def09b212.jpeg',
      '/homesweet/a1f09674-7bb5-4a59-b7d1-ce2c5521dfe1.jpeg',
      '/homesweet/34480425-676e-4c64-9f85-ae9c934c5312.jpeg',
      '/homesweet/f84a3f68-132e-455c-be67-2c58bf65c082.jpeg',
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
      '/homesweet/Gemini_Generated_Image_90wl9b90wl9b90wl.jpeg',
      '/homesweet/c02ffd00-ccf6-448e-a21c-6202e14a9340.jpeg',
      '/homesweet/cab57881-edf1-4915-a22b-a68cf4ebc688.jpeg',
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
      '/homesweet/Gemini_Generated_Image_laot81laot81laot.jpeg',
      '/homesweet/a1f09674-7bb5-4a59-b7d1-ce2c5521dfe1.jpeg',
      '/homesweet/465fdd21-b72c-4512-875f-ea562b99a5c1.jpeg',
      '/homesweet/740dbb11-17eb-4bf2-a6ef-eb5056550dbe.jpeg',
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
      '/homesweet/Gemini_Generated_Image_70bydd70bydd70by.jpeg',
      '/homesweet/86af45b4-efa9-4714-84bb-c02232f793cc.jpeg',
      '/homesweet/34480425-676e-4c64-9f85-ae9c934c5312.jpeg',
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
      '/homesweet/Gemini_Generated_Image_qz5tc7qz5tc7qz5t.jpeg',
      '/homesweet/cc362a63-5a5e-4f09-8722-cb6def09b212.jpeg',
      '/homesweet/a1f09674-7bb5-4a59-b7d1-ce2c5521dfe1.jpeg',
      '/homesweet/72ea68a6-2723-46a8-b29e-c60724e0e849.jpeg',
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
      '/homesweet/Gemini_Generated_Image_avafwoavafwoavaf.jpeg',
      '/homesweet/Gemini_Generated_Image_4slxg94slxg94slx.jpeg',
      '/homesweet/b389fd58-2a76-4d56-8190-cb65043ffea1.jpeg',
      '/homesweet/a492688d-f4de-4d9f-9077-0a0ba52fc44e.jpeg',
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

