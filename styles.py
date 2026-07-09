"""Styling constants for the digital twin Gradio app."""

BACKGROUND = "#FCFBFF"
SURFACE = "#FFFFFF"
PRIMARY = "#5B3CC4"
SECONDARY = "#8B5CF6"
ACCENT = "#E879F9"
TEXT = "#171717"
MUTED = "#807A94"
BORDER = "#ECE8F8"

EXAMPLES = [
  "Tell me about your background and experience.",
  "What kinds of projects are you working on now?",
  "What are your strongest technical skills?",
  "How can I get in touch with you?",
]

CSS = """
:root {
  --twin-bg: #FCFBFF;
  --twin-surface: #FFFFFF;
  --twin-primary: #5B3CC4;
  --twin-primary-hover: #4A2FA0;
  --twin-secondary: #8B5CF6;
  --twin-accent: #E879F9;
  --twin-text: #171717;
  --twin-muted: #807A94;
  --twin-border: #ECE8F8;
  --twin-shadow-primary: 91, 60, 196;
  --twin-shadow-secondary: 139, 92, 246;
  --twin-shadow-accent: 232, 121, 249;
  --twin-shadow-neutral: 34, 34, 34;
}

/* Dark mode: Gradio adds `.dark` to <body> when the browser/OS prefers dark
   (or the theme is forced dark). Same violet family, re-tuned for contrast
   on a deep background. */
body.dark {
  --twin-bg: #120E1F;
  --twin-surface: #1C1730;
  --twin-primary: #8B5CF6;
  --twin-primary-hover: #A78BFA;
  --twin-secondary: #C4B5FD;
  --twin-accent: #F0ABFC;
  --twin-text: #F2EEFB;
  --twin-muted: #9C93B5;
  --twin-border: #322C4D;
  --twin-shadow-primary: 139, 92, 246;
  --twin-shadow-secondary: 196, 181, 253;
  --twin-shadow-accent: 240, 171, 252;
  --twin-shadow-neutral: 0, 0, 0;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--twin-bg) !important; }

/* ---------- Layout: wider, more breathing room ---------- */
.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 1150px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 44px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 30px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  position: relative !important;
  display: inline-block !important;
  padding-bottom: 10px !important;
  margin: 4px 0 4px !important;
  text-align: left !important;
}
.gradio-container h1::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 56px;
  height: 4px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--twin-primary), var(--twin-accent));
}
.gradio-container .prose > *:not(h1) { color: var(--twin-muted) !important; }

/* ---------- Soft, rounded surfaces everywhere ---------- */
.block, .form {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  border-radius: 18px !important;
}

/* ---------- Hide the Chatbot label / header strip ---------- */
.twin-chatbot > .block-label,
.twin-chatbot > label,
.twin-chatbot .label-wrap,
.twin-chatbot .block-label,
.twin-chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame: elevated card ---------- */
.twin-chatbot {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 20px !important;
  min-height: 520px !important;
  box-shadow: 0 8px 28px rgba(var(--twin-shadow-primary), 0.08), 0 2px 8px rgba(var(--twin-shadow-neutral), 0.04) !important;
  padding: 4px !important;
}
.twin-chatbot .placeholder, .twin-chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Reset borders on every bubble variant first ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: none !important;
  border-radius: 16px !important;
  padding: 10px 14px !important;
}

/* ---------- Bubble backgrounds ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-primary) !important;
  color: #ffffff !important;
  border-radius: 16px 16px 4px 16px !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 16px 16px 16px 4px !important;
}

/* ---------- Accent stripe on assistant bubbles ----------
   Apply to every common bubble class for assistant rows, then suppress on
   any *nested* instance so the stripe lands on the outermost matching
   element only — exactly one stripe. */
.message-row.bot-row .message,
.message-row.bot-row .bubble,
.message-row.bot-row .message-bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .bubble,
.message-row[data-role="assistant"] .message-bubble {
  border-left: 3px solid var(--twin-accent) !important;
}

.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,
.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,
.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,
.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,
.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,
.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
}

/* ---------- Uniform font size in bubbles ----------
   Force every paragraph in a bubble to the same size. */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14.5px !important;
  line-height: 1.6 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14.5px !important;
  line-height: 1.6 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds from anything inside a bubble */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-accent) !important;
  text-decoration: underline;
}


/* input + button wrapper */
.gr-group, styler {
background: transparent !important;
border: none !important;
div {
background: transparent !important;
border: none !important;
}
}

/* ---------- Input row alignment ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
.input-container,
form[class*="input"] {
  align-items: stretch !important;
  gap: 12px !important;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}

textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 14px !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14.5px !important;
  padding: 13px 16px !important;
  line-height: 1.4 !important;
  min-height: 52px !important;
  box-shadow: 0 1px 3px rgba(var(--twin-shadow-neutral), 0.04) !important;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-primary) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(var(--twin-shadow-primary), 0.15) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 12px !important;
  background: var(--twin-surface) !important;
  color: var(--twin-text) !important;
  padding: 0 18px !important;
  min-height: 52px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease, transform 0.1s ease;
}
button:hover {
  border-color: var(--twin-secondary) !important;
  color: var(--twin-primary) !important;
  box-shadow: 0 2px 8px rgba(var(--twin-shadow-neutral), 0.06) !important;
}

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-primary) !important;
  border: 1px solid var(--twin-primary) !important;
  color: #ffffff !important;
  min-height: 52px !important;
  align-self: stretch !important;
  padding: 0 16px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 6px 16px rgba(var(--twin-shadow-primary), 0.28) !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: var(--twin-primary-hover) !important;
  border-color: var(--twin-primary-hover) !important;
  color: #ffffff !important;
  box-shadow: 0 8px 20px rgba(var(--twin-shadow-primary), 0.35) !important;
  transform: translateY(-1px);
}

/* ---------- Submit-button icon: center vertically and size correctly ---------- */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #ffffff !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples: soft pill chips ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 20px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; border-spacing: 8px !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  color: var(--twin-text) !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13.5px !important;
  font-weight: 400 !important;
  padding: 10px 18px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
  box-shadow: 0 1px 3px rgba(var(--twin-shadow-neutral), 0.04) !important;
  transition: border-color 0.15s ease, color 0.15s ease, box-shadow 0.15s ease;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-secondary) !important;
  color: var(--twin-primary) !important;
  background: var(--twin-surface) !important;
  box-shadow: 0 4px 12px rgba(var(--twin-shadow-secondary), 0.22) !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .twin-chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 10px !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 6px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .twin-chatbot .icon-button:hover {
  color: var(--twin-accent) !important;
  background: rgba(var(--twin-shadow-accent), 0.08) !important;
}

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-track { background: var(--twin-bg); }
::-webkit-scrollbar-thumb { background: var(--twin-border); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-secondary); }

/* ---------- Selection ---------- */
::selection { background: var(--twin-accent); color: #ffffff; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 28px 16px 40px !important; }
  .gradio-container h1 { font-size: 24px !important; }
  .twin-chatbot { min-height: 440px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
