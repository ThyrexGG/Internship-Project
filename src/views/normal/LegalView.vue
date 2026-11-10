<template>
  <div class="legal-page">
    <header class="legal-header">
      <button type="button" class="legal-back" @click="goBack">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M15 18l-6-6 6-6" />
        </svg>
        Back
      </button>
      <nav class="legal-tabs" aria-label="Legal documents">
        <router-link to="/privacy" class="legal-tab" :class="{ active: doc === 'privacy' }">Privacy Policy</router-link>
        <router-link to="/terms" class="legal-tab" :class="{ active: doc === 'terms' }">Terms of Use</router-link>
      </nav>
    </header>

    <main class="legal-main">
      <div class="legal-draft-note" role="note">
        <strong>Student project &mdash; draft document.</strong>
        HomeSweet is a course project, not a registered company. This text explains how the project handles data
        and what you can expect from it. It has not yet been reviewed by a lawyer.
      </div>

      <!-- ============ PRIVACY POLICY ============ -->
      <article v-if="doc === 'privacy'" class="legal-article">
        <h1>Privacy Policy</h1>
        <p class="legal-meta">Version {{ LEGAL_VERSION }} &middot; Last updated {{ LEGAL_UPDATED }}</p>

        <h2>1. Who we are</h2>
        <p>
          HomeSweet is a student housing and roommate web app built by a student team at CamTech as a university
          course project (FECO301). The team is responsible for the personal data described below. To ask a question or
          make a request, use <strong>Settings &rarr; Help</strong> in the app.
        </p>

        <h2>2. What we collect and why</h2>
        <div class="legal-table-wrap">
          <table class="legal-table">
            <thead>
              <tr><th>Data</th><th>Why we use it</th></tr>
            </thead>
            <tbody>
              <tr><td>Account details: name, email, role (tenant or landlord), sign-in method</td><td>To create and secure your account.</td></tr>
              <tr><td>Profile details you choose to add: phone, date of birth, gender, university, job, hobbies, photo</td><td>To show your profile and to suggest compatible roommates.</td></tr>
              <tr><td>Listings, photos, favourites, feed posts, friend requests, roommate requests</td><td>To run the marketplace and social features.</td></tr>
              <tr><td>Messages and attachments you send in chat</td><td>To deliver them to the person you are talking to.</td></tr>
              <tr><td>Rental applications, agreements and payment records</td><td>To process applications between tenants and landlords.</td></tr>
              <tr><td>Identity verification submission (only if you start it &mdash; see section 3)</td><td>To let a reviewer decide whether to award a verified badge.</td></tr>
            </tbody>
          </table>
        </div>
        <p>
          We do not sell your data and we do not use it for advertising. We only use it for the purposes in this table.
        </p>

        <h2>3. Identity verification (KYC)</h2>
        <ul>
          <li><strong>It is optional.</strong> You can use HomeSweet without verifying.</li>
          <li>
            <strong>Test mode.</strong> While the project is in its testing phase, verification is for usability testing only.
            You are asked to use a synthetic demo ID supplied by the team, <strong>not your real national ID, passport or
            face</strong>. In this mode your ID image is not sent to any third-party service.
          </li>
          <li>
            <strong>Live mode.</strong> Real identity checks will only be switched on after the team has finished its
            data-protection review. If that happens you will get a separate consent screen that states exactly what is
            collected, who can see it, and how long it is kept, and you can say no.
          </li>
          <li>
            In the current version the face comparison and liveness check run inside your browser. Your selfie is not
            uploaded or stored. Only the match result, a liveness yes/no, the document type and the submission time are saved.
          </li>
        </ul>

        <h2>4. Who can see your data</h2>
        <ul>
          <li><strong>Other users:</strong> your name, photo and the profile fields you fill in can be seen by signed-in users. Do not put information in your profile that you would not want other users to see.</li>
          <li><strong>The counterparty to a conversation or application:</strong> a landlord sees your application; a tenant sees a landlord's listing and profile.</li>
          <li><strong>Project administrators:</strong> a small number of team members who review verification requests, reports and abuse.</li>
          <li>
            <strong>Service providers (processors):</strong> we run on Google Firebase (authentication, database, file
            storage), which stores data on Google's servers, possibly outside Cambodia. Map and place features use
            Google Maps and OpenStreetMap when you use location search.
          </li>
        </ul>
        <p>We will disclose data to authorities only where the law requires it.</p>

        <h2>5. How long we keep it</h2>
        <ul>
          <li><strong>Account and profile data:</strong> until you delete your account, or until the course project ends and the test database is wiped, whichever is earlier.</li>
          <li><strong>Verification submissions:</strong> test-mode submissions are deleted when the test round that produced them is complete. If live mode is ever enabled, verification data will be deleted within 30 days of a decision unless the law requires otherwise.</li>
          <li><strong>Chat messages and applications:</strong> until you or the other person deletes them, or the account is deleted.</li>
          <li><strong>Payment records:</strong> the project currently runs demonstration payments only. No real money moves through HomeSweet.</li>
        </ul>

        <h2>6. Your choices</h2>
        <p>
          You can ask to see, correct, export or delete the data we hold about you, and you can withdraw consent at any
          time. Withdrawing consent does not affect what we did before. Contact us through Settings &rarr; Help. We aim to
          answer within 30 days. You can also edit most profile data yourself in Settings.
        </p>

        <h2>7. Security</h2>
        <p>
          Data is sent over HTTPS and access is limited by sign-in and database security rules. No system is perfectly
          secure, and this is a student-built prototype: please do not share anything you are not comfortable sharing.
          If we learn of a breach affecting your data we will tell affected users without undue delay.
        </p>

        <h2>8. Children</h2>
        <p>HomeSweet is for people aged 18 and over. Do not create an account if you are younger.</p>

        <h2>9. Changes to this policy</h2>
        <p>
          We will update this page and its version number when practice changes. For material changes, such as turning on
          live identity checks, we will ask for your consent again.
        </p>
      </article>

      <!-- ============ TERMS OF USE ============ -->
      <article v-else class="legal-article">
        <h1>Terms of Use</h1>
        <p class="legal-meta">Version {{ LEGAL_VERSION }} &middot; Last updated {{ LEGAL_UPDATED }}</p>

        <h2>1. What HomeSweet is</h2>
        <p>
          HomeSweet is a platform that helps students find rooms, landlords advertise them, and students find roommates.
          It is a student course project provided as-is and may change or be taken down at any time.
        </p>

        <h2>2. HomeSweet is not a party to your rental</h2>
        <ul>
          <li>Any lease is an agreement <strong>only between the landlord and the tenant</strong>. HomeSweet is not the landlord, agent, broker or guarantor.</li>
          <li>HomeSweet does <strong>not</strong> hold deposits in escrow and does not process real payments. Any payment screen is a demonstration.</li>
          <li>Agreement templates and the in-app lease preview are <strong>illustrative only</strong>. They are not legal advice. Get your own advice and sign a proper lease before paying money or moving in.</li>
          <li>Always view a property in person and confirm the landlord's identity and right to let it before you pay anything.</li>
        </ul>

        <h2>3. Verification badges</h2>
        <p>
          A &ldquo;verified&rdquo; badge means a reviewer checked some information at a point in time. It is not a guarantee of
          identity, honesty, safety or the condition of a property. Use your own judgement.
        </p>

        <h2>4. Your account</h2>
        <ul>
          <li>You must be 18 or over and give accurate information.</li>
          <li>Keep your password private. You are responsible for activity on your account.</li>
          <li>One person, one account. Do not impersonate anyone.</li>
        </ul>

        <h2>5. Rules for everyone</h2>
        <p>You agree not to:</p>
        <ul>
          <li>post false, misleading or fraudulent listings, prices, photos or profiles;</li>
          <li>harass, threaten, discriminate against or spam other users;</li>
          <li>upload someone else's ID, photos or personal data without their permission;</li>
          <li>upload your own real government ID while verification is in test mode;</li>
          <li>scrape the service, probe or bypass its security, or use it for anything unlawful.</li>
        </ul>
        <p>We may remove content or suspend accounts that break these rules.</p>

        <h2>6. Landlords</h2>
        <ul>
          <li>You confirm you have the right to let any property you list.</li>
          <li>Listings must be accurate and kept up to date, including rent, deposit, house rules and availability.</li>
          <li>You are responsible for your own tenancy paperwork and for complying with the law that applies to your lease.</li>
          <li>Treat tenant applications and documents as confidential. Use them only to decide on the application.</li>
        </ul>

        <h2>7. Your content</h2>
        <p>
          You keep ownership of what you post. You give HomeSweet a non-exclusive licence to store and display it inside the
          service so the features work. You promise you have the right to post it.
        </p>

        <h2>8. Liability</h2>
        <p>
          The service is provided &ldquo;as is&rdquo;. To the extent the law allows, the project team is not liable for losses
          arising from your use of HomeSweet, including disputes between tenants and landlords, inaccurate listings, or
          the service being unavailable. Nothing in these terms limits any liability that cannot be limited by law.
        </p>

        <h2>9. Governing law</h2>
        <p>These terms are governed by the laws of the Kingdom of Cambodia.</p>

        <h2>10. Changes and contact</h2>
        <p>
          We may update these terms and will change the version above when we do. If you keep using HomeSweet after a
          change you accept the new version. Questions: Settings &rarr; Help.
        </p>
      </article>

      <p class="legal-footer-link">
        Related: <router-link :to="doc === 'privacy' ? '/terms' : '/privacy'">{{ doc === 'privacy' ? 'Terms of Use' : 'Privacy Policy' }}</router-link>
      </p>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { LEGAL_VERSION, LEGAL_UPDATED } from '../../config/legal'

const route = useRoute()
const router = useRouter()

const doc = computed(() => (route.name === 'Terms' ? 'terms' : 'privacy'))

function goBack() {
  if (window.history.length > 1) router.back()
  else router.push('/home')
}
</script>

<style scoped>
.legal-page {
  min-height: 100vh;
  background: var(--color-bg-canvas, #faf8f5);
  color: var(--color-text-primary, #2A2421);
  font-family: var(--font-body, 'DM Sans', sans-serif);
}
.legal-header {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 12px 16px;
  background: #fff;
  border-bottom: 1px solid var(--color-border, #ede8e3);
}
.legal-back {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  border: none;
  background: none;
  font: inherit;
  font-weight: 600;
  color: var(--color-primary, #5C4E4E);
  cursor: pointer;
  padding: 8px 4px;
}
.legal-tabs { display: flex; gap: 6px; }
.legal-tab {
  padding: 8px 14px;
  border-radius: var(--radius-pill, 50px);
  font-size: 0.875rem;
  font-weight: 600;
  text-decoration: none;
  color: var(--color-text-secondary, #5C4E4E);
}
.legal-tab.active {
  background: var(--color-primary, #5C4E4E);
  color: #fff;
}
.legal-main {
  max-width: 760px;
  margin: 0 auto;
  padding: 24px 16px 64px;
}
.legal-draft-note {
  background: var(--color-warning-bg, #FEF3C7);
  color: #78350F;
  border-radius: var(--radius-md, 10px);
  padding: 12px 14px;
  font-size: 0.875rem;
  line-height: 1.5;
  margin-bottom: 24px;
}
.legal-article {
  background: #fff;
  border-radius: var(--radius-xl, 18px);
  box-shadow: var(--shadow-elevation-1, 0 1px 3px rgba(42,36,33,.05));
  padding: 24px 20px;
}
.legal-article h1 {
  font-family: var(--font-serif, Georgia, serif);
  font-size: 1.9rem;
  margin: 0 0 4px;
}
.legal-meta { color: #6B5D5D; font-size: 0.8125rem; margin: 0 0 20px; }
.legal-article h2 { font-size: 1.05rem; margin: 24px 0 8px; }
.legal-article p,
.legal-article li { font-size: 0.9375rem; line-height: 1.65; color: var(--color-text-secondary, #5C4E4E); }
.legal-article ul { padding-left: 20px; margin: 8px 0; }
.legal-article li { margin-bottom: 6px; }
.legal-table-wrap { overflow-x: auto; }
.legal-table { width: 100%; border-collapse: collapse; font-size: 0.875rem; }
.legal-table th,
.legal-table td {
  text-align: left;
  vertical-align: top;
  padding: 10px 12px;
  border-bottom: 1px solid var(--color-border, #ede8e3);
  color: var(--color-text-secondary, #5C4E4E);
}
.legal-table th { color: var(--color-text-primary, #2A2421); background: var(--color-primary-light, #F2EDE9); }
.legal-footer-link { margin-top: 20px; font-size: 0.875rem; text-align: center; }
.legal-footer-link a { color: var(--color-primary, #5C4E4E); font-weight: 600; }

@media (min-width: 640px) {
  .legal-article { padding: 32px 36px; }
}
</style>
