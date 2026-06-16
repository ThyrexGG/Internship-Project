import { createRouter, createWebHistory } from 'vue-router'
import LoginView from './views/normal/LoginView.vue'
import HomeView from './views/normal/HomeView.vue'
import LandlordNotification from './views/landlord/LandlordNotification.vue'
import VerifyAccountView from './views/normal/VerifyAccountView.vue'
import SetupAccountView from './views/normal/SetupAccountView.vue'
import PropertyDetailView from './views/normal/PropertyDetailView.vue'
import LandlordProfileView from './views/landlord/LandlordProfileView.vue'

import FindRoommateView from './views/normal/FindRoommateView.vue'
import RoommateMatchView from './views/normal/RoommateMatchView.vue'
import SearchResultsView from './views/normal/SearchResultsView.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginView },
  { path: '/home', component: HomeView },
  { path: '/landlord', component: LandlordNotification },
  { path: '/verify-account', component: VerifyAccountView },
  { path: '/setup-account', component: SetupAccountView },
  { path: '/property/:id', name: 'PropertyDetail', component: PropertyDetailView },
  { path: '/property/:id/roommate', name: 'FindRoommate', component: FindRoommateView },
  { path: '/roommate-match', name: 'RoommateMatch', component: RoommateMatchView },
  { path: '/landlord-profile/:id', name: 'LandlordProfile', component: LandlordProfileView },
  { path: '/search', name: 'SearchResults', component: SearchResultsView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})