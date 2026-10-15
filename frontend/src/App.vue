<script setup>
import { ref, onMounted } from 'vue'

const documents = ref([])

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/documents')

    if (!response.ok) {
      throw new Error('Erreur lors de la récupération des documents')
    }

    documents.value = await response.json()
  } catch (error) {
    console.error('Erreur API :', error)
  }
})
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

          <button class="upload-button">
            Choisir un fichier
          </button>
        </div>
      </section>

      <section class="documents-section">
        <h2>Mes documents</h2>

        <div
  v-for="document in documents"
  :key="document.id"
  class="document-card"
>
  <span class="file-icon">📄</span>

  <div class="document-info">
    <strong>{{ document.filename }}</strong>
    <span>
      Ajouté le {{ new Date(document.created_at).toLocaleDateString('fr-FR') }}
    </span>
  </div>

  <span class="status">✓</span>
</div>  
      </section>

      <section class="question-section">
        <h2>Posez une question</h2>

        <div class="question-box">
          <input
            type="text"
            placeholder="Posez une question à votre document..."
          />

          <button class="question-button">
            Demander
          </button>
        </div>
      </section>
    </main>
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
  max-width: 900px;
  margin: 50px auto;
  padding: 0 20px;
}

.upload-section {
  text-align: center;
}

.upload-section h1 {
  font-size: 36px;
  margin-bottom: 10px;
}

.description {
  color: #6b7280;
  margin-bottom: 30px;
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
}

button {
  border: none;
  border-radius: 8px;
  padding: 12px 20px;
  font-size: 15px;
  cursor: pointer;
}

.upload-button,
.question-button {
  background: #111827;
  color: white;
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
  flex-direction: column;
  flex: 1;
}

.document-info span {
  margin-top: 4px;
  color: #6b7280;
  font-size: 14px;
}

.status {
  font-size: 20px;
}

.question-box {
  display: flex;
  gap: 10px;
}

.question-box input {
  flex: 1;
  padding: 14px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 15px;
}
</style>
```
