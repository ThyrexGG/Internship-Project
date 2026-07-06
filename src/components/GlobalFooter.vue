<template>
  <footer class="site-footer">
    <div class="footer-columns">
      <div class="footer-col">
        <h4>Support</h4>
        <ul>
          <li><a href="#">Help Center</a></li>
          <li><a href="#">Safety information</a></li>
          <li><a href="#">Cancellation options</a></li>
          <li><a href="#">Report a concern</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Hosting</h4>
        <ul>
          <li><a href="#">Nomad your home</a></li>
          <li><a href="#">Hosting resources</a></li>
          <li><a href="#">Community forum</a></li>
          <li><a href="#">Hosting responsibly</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Nomad</h4>
        <ul>
          <li><a href="#">Newsroom</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Investors</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-legal">
        © 2026 Nomad, Inc. · <a href="#">Privacy</a> · <a href="#">Terms</a> · <a href="#">Your Privacy Choices</a>
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

.footer-columns {
  display: grid;
  grid-template-columns: 1fr; /* Single column on mobile */
  gap: 24px;
  border-bottom: 1px solid #D1D0D0;
  padding-bottom: 24px;
  margin-bottom: 24px;
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
  .footer-columns {
    grid-template-columns: repeat(3, 1fr);
  }
  .footer-bottom {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}
</style>
