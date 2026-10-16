(() => {
  'use strict';
  const websitePrice = pages => pages === 1 ? 499 : pages === 2 ? 1000 : pages * 500 - 1;
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('navigation');
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {
      menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); menu.focus();
    }
  });
  const count = document.getElementById('page-count');
  if (count) {
    const rateInput = document.getElementById('exchange-rate');
    const status = document.getElementById('rate-status');
    const refresh = document.getElementById('refresh-rate');
    const snapshot = {rate:63.084291, updated:'2026-10-16T00:02:31Z', expires:0};
    const key = 'xander-usd-php-v1';
    let reference = snapshot;
    let manual = false;
    let controller;
    const usd = new Intl.NumberFormat('en-US',{style:'currency',currency:'USD'});
    const php = new Intl.NumberFormat('en-PH',{style:'currency',currency:'PHP'});
    const dateLabel = date => new Date(date).toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'});
    function validRate(n) { return Number.isFinite(n) && n > 0 && n <= 1000; }
    function pages() { return Math.min(50,Math.max(1,Math.round(Number(count.value) || 1))); }
    function render() {
      const n = pages();
      const rate = Number(rateInput.value);
      const total = websitePrice(n);
      document.getElementById('usd-total').textContent = 'US' + usd.format(total);
      document.getElementById('php-total').textContent = validRate(rate) ? php.format(total * rate) : 'Enter a valid rate';
      document.getElementById('price-formula').textContent = `${n}-page website package`;
      document.getElementById('pages-less').disabled = n <= 1;
      document.getElementById('pages-more').disabled = n >= 50;
      document.getElementById('estimate-inquiry').href = `contact.html?pages=${n}#inquiry`;
    }
    function useReference(data, prefix) {
      reference = data; manual = false; rateInput.value = data.rate;
      status.textContent = `${prefix} · ${dateLabel(data.updated)}. You can edit it.`;
      render();
    }
    async function loadRate(force=false) {
      if (force) manual = false;
      refresh.disabled = true;
      refresh.setAttribute('aria-busy','true');
      status.textContent = 'Checking the latest daily exchange rate…';
      controller?.abort(); controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), 8000);
      try {
        if (!force) {
          let cached;
          try { cached = JSON.parse(localStorage.getItem(key)); } catch (_) {}
          if (cached && validRate(cached.rate) && Number.isFinite(Date.parse(cached.updated)) && cached.expires > Date.now()) {
            if (!manual) useReference(cached,'Latest daily rate');
            return;
          }
        }
        const response = await fetch('https://open.er-api.com/v6/latest/USD',{signal:controller.signal});
        if (!response.ok) throw new Error('Rate service unavailable');
        const data = await response.json();
        if (data.result !== 'success' || data.base_code !== 'USD' || !validRate(data.rates?.PHP) || !Number.isFinite(data.time_last_update_unix)) throw new Error('Invalid exchange rate');
        const latest = {rate:data.rates.PHP,updated:new Date(data.time_last_update_unix * 1000).toISOString(),expires:Math.min(Number(data.time_next_update_unix)*1000 || Date.now()+3600000, Date.now()+86400000)};
        try { localStorage.setItem(key,JSON.stringify(latest)); } catch (_) {}
        if (!manual) useReference(latest,'Latest daily rate');
      } catch (_) {
        if (!manual) useReference(reference,'Saved reference rate; refresh unavailable');
      } finally {
        clearTimeout(timeout); refresh.disabled = false; refresh.removeAttribute('aria-busy');
      }
    }
    count.addEventListener('input',render);
    count.addEventListener('change',()=>{count.value=pages();render();});
    for (const [id,step] of [['pages-less',-1],['pages-more',1]]) document.getElementById(id).addEventListener('click',()=>{count.value=pages()+step;render();});
    rateInput.addEventListener('input',()=>{manual=true;status.textContent='Your custom exchange rate. PHP is an estimate; confirm the final amount with Xander.';render();});
    rateInput.addEventListener('change',()=>{if(!validRate(Number(rateInput.value))){rateInput.value=reference.rate;manual=false;status.textContent=`Saved reference rate · ${dateLabel(reference.updated)}. You can edit it.`;}render();});
    refresh.addEventListener('click',()=>loadRate(true));
    render();loadRate();
  }
  const form = document.getElementById('inquiry-form');
  if (form) {
    const pagesInput = document.getElementById('inquiry-pages');
    const supplied = Number(new URLSearchParams(location.search).get('pages'));
    if (Number.isInteger(supplied) && supplied >= 1 && supplied <= 50) pagesInput.value=supplied;
    form.addEventListener('submit',event=>{
      event.preventDefault();
      if(!form.reportValidity()) return;
      const name = document.getElementById('client-name').value.trim();
      const type = document.getElementById('project-type').value;
      const n=Number(pagesInput.value);
      const message=document.getElementById('project-message').value.trim();
      const feedback=type==='General inquiry or feedback';
      const subject=feedback ? `Portfolio inquiry from ${name}` : `Website inquiry: ${type} (${n} ${n===1?'page':'pages'})`;
      const body=`Hi Xander,\n\nMy name is ${name}.\n\n${feedback?'Inquiry or feedback':`Project type: ${type}\nEstimated pages: ${n}\nWebsite package price: US$${websitePrice(n).toLocaleString('en-US')}`}\n\n${message}\n\nThank you,\n${name}`;
      document.getElementById('form-status').textContent='Your email draft is ready. Review it in your email app and press Send. If it does not open, email xandersolancho21@gmail.com directly.';
      window.location.href=`mailto:xandersolancho21@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  }
})();
