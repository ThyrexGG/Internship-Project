import { createRouter, createWebHistory } from 'vue-router'
import LoginView from './views/LoginView.vue'
import HomeView from './views/HomeView.vue'
import LandlordNotification from './views/LandlordNotification.vue'
import VerifyAccountView from './views/VerifyAccountView.vue'
import PropertyDetailView from './views/PropertyDetailView.vue'

import FindRoommateView from './views/FindRoommateView.vue'
import RoommateMatchView from './views/RoommateMatchView.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginView },
  { path: '/home', component: HomeView },
  { path: '/landlord', component: LandlordNotification },
  { path: '/verify-account', component: VerifyAccountView },
  { path: '/property/:id', name: 'PropertyDetail', component: PropertyDetailView },
  { path: '/property/:id/roommate', name: 'FindRoommate', component: FindRoommateView },
  { path: '/roommate-match', name: 'RoommateMatch', component: RoommateMatchView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})