```vue
<script setup>
import { ref } from 'vue'

const selectedFile = ref(null)
const question = ref('')
const message = ref('')

function handleFileChange(event) {
  selectedFile.value = event.target.files[0] || null
  message.value = ''
}

function askQuestion() {
  if (!selectedFile.value || !question.value.trim()) return

  message.value =
    "L'analyse IA sera disponible lorsque le backend Flask sera connecté."
}
</script>

<template>
  <div class="app">
    <header class="header">
      <div class="logo">
        <span class="logo-icon">📄</span>
        <span>Doc Expert AI</span>
      </div>

      <p class="subtitle">
        Votre assistant intelligent pour vos documents
      </p>
    </header>

    <main class="main">
      <section class="upload-section">
        <h1>Analysez vos documents</h1>

        <p class="description">
          Importez un document et posez ensuite vos questions à son sujet.
        </p>

        <div class="upload-box">
          <div class="upload-icon">📄</div>

          <h2>Déposez votre document ici</h2>

          <p>ou choisissez un fichier depuis votre ordinateur</p>

          <input
            id="file-input"
            type="file"
            accept=".pdf,.txt,.doc,.docx"
            hidden
            @change="handleFileChange"
          />

          <label for="file-input" class="upload-button">
            Choisir un fichier
          </label>

          <p v-if="selectedFile" class="file-selected">
            Fichier sélectionné : {{ selectedFile.name }}
          </p>
        </div>
      </section>

      <section class="documents-section">
        <h2>Mes documents</h2>

        <div v-if="selectedFile" class="document-card">
          <span class="file-icon">📄</span>

          <div class="document-info">
            <strong>{{ selectedFile.name }}</strong>
            <span>Fichier sélectionné sur votre ordinateur</span>
          </div>

          <span class="status">✓</span>
        </div>

        <p v-else class="empty-state">
          Aucun document sélectionné pour le moment.
        </p>
      </section>

      <section class="question-section">
        <h2>Posez une question</h2>

        <div class="question-box">
          <input
            v-model="question"
            type="text"
            placeholder="Posez une question à votre document..."
            @keyup.enter="askQuestion"
          />

          <button
            class="question-button"
            :disabled="!selectedFile || !question.trim()"
            @click="askQuestion"
          >
            Demander
          </button>
        </div>

        <p v-if="message" class="message">
          {{ message }}
        </p>

        <p v-else class="helper-text">
          Sélectionnez un document pour préparer votre question.
        </p>
      </section>
    </main>

    <footer class="footer">
      Doc Expert AI · Projet en cours de développement
    </footer>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
}

.app {
  min-height: 100vh;
  background: #f6f7fb;
  color: #1f2937;
  font-family: Arial, sans-serif;
}

.header {
  padding: 30px 8%;
  background: white;
  border-bottom: 1px solid #e5e7eb;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 24px;
  font-weight: bold;
}

.logo-icon {
  font-size: 28px;
}

.subtitle {
  margin: 8px 0 0 38px;
  color: #6b7280;
}

.main {
  width: 100%;
  max-width: 900px;
  margin: 50px auto;
  padding: 0 20px;
}

.upload-section {
  text-align: center;
}

.upload-section h1 {
  margin-bottom: 10px;
  font-size: 36px;
}

.description {
  margin-bottom: 30px;
  color: #6b7280;
  line-height: 1.6;
}

.upload-box {
  padding: 50px 30px;
  background: white;
  border: 2px dashed #cbd5e1;
  border-radius: 16px;
}

.upload-icon {
  font-size: 45px;
}

.upload-box h2 {
  margin: 15px 0 8px;
}

.upload-box p {
  color: #6b7280;
  overflow-wrap: anywhere;
}

.upload-button,
.question-button {
  display: inline-block;
  padding: 12px 20px;
  border: none;
  border-radius: 8px;
  background: #111827;
  color: white;
  font-size: 15px;
  cursor: pointer;
  transition: background 0.2s ease;
}

.upload-button {
  margin-top: 12px;
}

.upload-button:hover,
.question-button:hover:not(:disabled) {
  background: #374151;
}

.file-selected {
  margin-top: 18px;
}

.documents-section,
.question-section {
  margin-top: 40px;
}

.documents-section h2,
.question-section h2 {
  margin-bottom: 15px;
}

.document-card {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 18px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
}

.file-icon {
  font-size: 25px;
}

.document-info {
  display: flex;
  flex: 1;
  flex-direction: column;
  min-width: 0;
  overflow-wrap: anywhere;
}

.document-info span {
  margin-top: 4px;
  color: #6b7280;
  font-size: 14px;
}

.status {
  color: #16a34a;
  font-size: 20px;
}

.empty-state,
.helper-text,
.message {
  color: #6b7280;
  font-size: 14px;
  line-height: 1.6;
}

.question-box {
  display: flex;
  gap: 10px;
}

.question-box input {
  flex: 1;
  min-width: 0;
  padding: 14px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 15px;
}

.question-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.helper-text,
.message {
  margin-top: 12px;
}

.message {
  color: #374151;
}

.footer {
  padding: 25px 20px;
  color: #6b7280;
  font-size: 13px;
  text-align: center;
}

@media (max-width: 600px) {
  .header {
    padding: 24px 20px;
  }

  .logo {
    font-size: 21px;
  }

  .subtitle {
    margin-left: 0;
  }

  .main {
    margin: 35px auto;
  }

  .upload-section h1 {
    font-size: 28px;
  }

  .upload-box {
    padding: 35px 18px;
  }

  .question-box {
    flex-direction: column;
  }

  .question-box input,
  .question-button {
    width: 100%;
  }
}
</style>
```
