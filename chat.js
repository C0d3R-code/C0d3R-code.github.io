(() => {
  const launcher = document.getElementById('chat-launcher');
  const panel = document.getElementById('chat-panel');
  const close = document.getElementById('chat-close');
  const messages = document.getElementById('chat-messages');
  const form = document.getElementById('chat-form');
  const input = document.getElementById('chat-input');
  const send = form.querySelector('button[type="submit"]');
  const status = document.getElementById('chat-status');
  const note = document.getElementById('chat-note');
  const history = [];
  let aiEnabled = false;

  function addMessage(text, who) {
    const item = document.createElement('div');
    item.className = `chat-message ${who}`;
    item.textContent = text;
    messages.appendChild(item);
    messages.scrollTop = messages.scrollHeight;
  }

  function quickAnswer(question) {
    const q = question.toLowerCase();
    if (/contact|email|phone|call|reach|hire|inquiry|feedback/.test(q)) {
      return 'You can reach Xander at xandersolancho21@gmail.com or +63 977 776 3279. For project inquiries and feedback, email is best.';
    }
    if (/project|build|portfolio|work|snake|restaurant|library|converter|traffic/.test(q)) {
      return 'Xander has featured a C++ Snake game, a Python restaurant ordering system, two Java applications, and an Arduino traffic light sketch. The Projects section has local source links.';
    }
    if (/skill|language|technology|tech|experience|java|python|arduino|c\+\+/.test(q)) {
      return 'His projects show C++, Python, Java, Arduino, data structures, object-oriented programming, command-line applications, and hardware control.';
    }
    if (/school|student|study|university|feu/.test(q)) {
      return 'Xander is a software engineering student at FEU Tech. The portfolio features selected coursework and coding practice.';
    }
    return 'I can answer quick questions about Xander’s projects, skills, and contact details. For a specific proposal or feedback, email xandersolancho21@gmail.com.';
  }

  async function checkAiStatus() {
    if (location.protocol === 'file:') return;
    try {
      const response = await fetch('api/status', { cache: 'no-store' });
      if (!response.ok) return;
      const data = await response.json();
      if (data.enabled === true) {
        aiEnabled = true;
        status.textContent = 'AI replies to questions about Xander’s work';
        note.innerHTML = 'AI replies may be inaccurate. Messages are processed by OpenAI. For inquiries, <a href="mailto:xandersolancho21@gmail.com?subject=Portfolio%20inquiry">email Xander</a>.';
      }
    } catch (_) {
      // The static preview and GitHub Pages work without an AI endpoint.
    }
  }

  async function answer(question) {
    if (!aiEnabled) return quickAnswer(question);
    const response = await fetch('api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: question, history: history.slice(-6) })
    });
    if (!response.ok) throw new Error('AI endpoint unavailable');
    const data = await response.json();
    if (typeof data.reply !== 'string' || !data.reply.trim()) throw new Error('Empty AI reply');
    return data.reply.trim();
  }

  async function submitQuestion(question) {
    const clean = question.trim().slice(0, 500);
    if (!clean) return;
    addMessage(clean, 'user');
    input.value = '';
    input.disabled = true;
    send.disabled = true;
    try {
      const reply = await answer(clean);
      addMessage(reply, 'bot');
      history.push({ role: 'user', content: clean }, { role: 'assistant', content: reply });
    } catch (_) {
      addMessage('The AI service is temporarily unavailable. You can email Xander at xandersolancho21@gmail.com or call +63 977 776 3279.', 'bot');
    } finally {
      input.disabled = false;
      send.disabled = false;
      input.focus();
    }
  }

  function setOpen(open) {
    panel.hidden = !open;
    launcher.setAttribute('aria-expanded', String(open));
    if (open) input.focus(); else launcher.focus();
  }

  launcher.addEventListener('click', () => setOpen(panel.hidden));
  close.addEventListener('click', () => setOpen(false));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !panel.hidden) setOpen(false);
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    submitQuestion(input.value);
  });
  panel.querySelectorAll('[data-question]').forEach(button => {
    button.addEventListener('click', () => submitQuestion(button.dataset.question));
  });
  checkAiStatus();
})();
