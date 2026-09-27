<template>
  <footer class="site-footer">
    <div class="footer-top">
      <div class="footer-brand">
        <div class="footer-logo">
          <div class="footer-logo-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 18 L16 18" />
              <path d="M4 18 L4 12 L9 7 L16 14" />
              <path d="M12 18 L12 4 L16 4 L16 18 Z" />
              <path d="M12 14 L16 14" />
            </svg>
          </div>
          <span class="footer-logo-text">HomeSweet</span>
        </div>
        <p class="footer-tagline">Find your next home, roommate, and rental — all in one place.</p>
      </div>

      <div class="footer-columns">
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="#">Help Center</a></li>
            <li><a href="#">Safety Information</a></li>
            <li><a href="#">Cancellation Options</a></li>
            <li><a href="#">Report a Concern</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>For Landlords</h4>
          <ul>
            <li><a href="#">Become a Host</a></li>
            <li><a href="#">Hosting Resources</a></li>
            <li><a href="#">Community Forum</a></li>
            <li><a href="#">Hosting Responsibly</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="#">About HomeSweet</a></li>
            <li><a href="#">Newsroom</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Investors</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-legal">
        © 2026 HomeSweet, Inc. · <a href="#">Privacy</a> · <a href="#">Terms</a> · <a href="#">Your Privacy Choices</a>
      </div>
      <div class="footer-social">
        <span class="language">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align: middle; margin-right: 4px;"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          English (US)
        </span>
        <span class="currency">$ USD</span>
      </div>
    </div>
  </footer>
</template>

<style scoped>
/* Footer Styles */
.site-footer {
  background: #ffffff !important;
  border-top: 1px solid #988686 !important;
  padding: 32px 16px 80px; /* Extra padding on bottom for bottom-nav */
  margin-top: 24px;
  font-family: inherit;
  color: #000000;
}

.footer-top {
  display: flex;
  flex-direction: column;
  gap: 28px;
  border-bottom: 1px solid #D1D0D0;
  padding-bottom: 24px;
  margin-bottom: 24px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 8px;
}

.footer-logo-icon {
  display: flex;
  align-items: center;
  color: #5C4E4E;
}

.footer-logo-text {
  font-size: 1.15rem;
  font-weight: 700;
  color: #2A2421;
  letter-spacing: -0.3px;
}

.footer-tagline {
  margin: 10px 0 0;
  font-size: 0.88rem;
  color: #5C4E4E;
  max-width: 360px;
  line-height: 1.5;
}

.footer-columns {
  display: grid;
  grid-template-columns: 1fr; /* Single column on mobile */
  gap: 24px;
}

.footer-col h4 {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: #000000;
}

.footer-col ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-col ul li {
  margin-bottom: 12px;
}

.footer-col ul li a {
  text-decoration: none;
  color: #5C4E4E;
  font-size: 0.9rem;
  transition: color 0.2s;
}

.footer-col ul li a:hover {
  text-decoration: underline;
  color: #000000;
}

.footer-bottom {
  display: flex;
  flex-direction: column;
  gap: 16px;
  font-size: 0.85rem;
  color: #5C4E4E;
}

.footer-legal a {
  text-decoration: none;
  color: #5C4E4E;
  margin: 0 4px;
}

.footer-legal a:hover {
  text-decoration: underline;
  color: #000000;
}

.footer-social {
  display: flex;
  align-items: center;
  gap: 16px;
  font-weight: 600;
  color: #000000;
}

.footer-social .language, .footer-social .currency {
  cursor: pointer;
}

@media (min-width: 768px) {
  .site-footer {
    padding: 48px 40px 24px;
  }
  .footer-top {
    flex-direction: row;
    justify-content: space-between;
    gap: 40px;
  }
  .footer-brand {
    flex-shrink: 0;
    max-width: 280px;
  }
  .footer-columns {
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    flex: 1;
    max-width: 560px;
  }
  .footer-bottom {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}
</style>
