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
import UserProfileView from './views/normal/UserProfileView.vue'
import RentalApplicationView from './views/normal/RentalApplicationView.vue'
import PaymentView from './views/normal/PaymentView.vue'
import ChatView from './views/normal/ChatView.vue'
import AdminPortalView from './views/admin/AdminPortalView.vue'

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
  { path: '/user-profile/:id', name: 'UserProfile', component: UserProfileView },
  { path: '/search', name: 'SearchResults', component: SearchResultsView },
  { path: '/property/:id/apply', name: 'RentalApplication', component: RentalApplicationView },
  { path: '/payment', name: 'Payment', component: PaymentView },
  { path: '/property/:id/payment', name: 'PropertyPayment', component: PaymentView },
  { path: '/checkout', redirect: '/payment' },
  { path: '/chat', name: 'Chat', component: ChatView },
  { path: '/messages', redirect: '/chat' },
  { path: '/admin', name: 'AdminPortal', component: AdminPortalView },
  { path: '/admin/login', redirect: '/admin' },
  { path: '/admin/verifications', name: 'AdminVerifications', component: AdminPortalView },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})