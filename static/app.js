const chatWindow = document.getElementById('chat-window');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const languageSelect = document.getElementById('language-select');
const btnHelp = document.getElementById('btn-help');
const btnEvents = document.getElementById('btn-events');
const btnAccommodation = document.getElementById('btn-accommodation');
const btnTranslate = document.getElementById('btn-translate');

function appendMessage(text, type) {
  const bubble = document.createElement('div');
  bubble.className = `message ${type}`;
  bubble.textContent = text;
  chatWindow.appendChild(bubble);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendChat(message) {
  if (!message.trim()) return;
  appendMessage(message, 'user');
  messageInput.value = '';
  sendButton.disabled = true;

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message,
        language: languageSelect.value,
      }),
    });

    if (!response.ok) {
      appendMessage('Sorry, the assistant is unavailable right now.', 'assistant');
      return;
    }

    const data = await response.json();
    appendMessage(data.reply, 'assistant');
  } catch (error) {
    appendMessage('Unable to reach the assistant. Please make sure the server is running.', 'assistant');
  } finally {
    sendButton.disabled = false;
  }
}

sendButton.addEventListener('click', () => sendChat(messageInput.value));
messageInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    sendChat(messageInput.value);
  }
});

btnHelp.addEventListener('click', () => sendChat('I need emergency help.'));
btnEvents.addEventListener('click', () => sendChat('What is the event schedule?'));
btnAccommodation.addEventListener('click', () => sendChat('Where can I stay near the festival?'));
btnTranslate.addEventListener('click', () => sendChat('Translate thank you to ' + languageSelect.value));

appendMessage('Hello pilgrim! Select your language and ask me anything about Mahakumbh, from directions to emergency support. I also support French, Japanese, and German translations.', 'assistant');
