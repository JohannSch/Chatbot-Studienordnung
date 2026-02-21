<template>
  <div id="input-main">
    <div id="conversation-container">
      <div v-for="message in conversation" :class="message.type" v-html="message.text"></div>
    </div>
    
    <div>
      <input class="input-field" ref="input_field" @keyup.enter="submit" @keyup.escape="input_field.blur();" type="text" placeholder="Gib eine Frage ein" v-model="question">
    </div>
  </div>
</template>

<script setup>

import { ref } from 'vue';
import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js"; // danke an Frederic fürs finden dieser Lib


const input_field = ref(null);

const question = ref('');
const conversation = ref([]);

const API_AI_RESPONSE = 'http://127.0.0.1:8000/ai-response';


async function submit(){

  const url = API_AI_RESPONSE + '?question=' + question.value;

  conversation.value.push(JSON.parse(JSON.stringify({text: question.value, type: "question"})));

  try{
    const response = await fetch(url, {method: "GET"});
    if (!response.ok) {throw new Error(`Response status: ${response.status}`);}

    const data = await response.json();
    console.log(data);

    conversation.value.push(JSON.parse(JSON.stringify({text: marked.parse(data), type: "ai_response"})));
  }
  catch(error){
    console.error(error.message);
    return;
  }
}

</script>

<style scoped>

#input-main {
  height: 80%;
  width: inherit;
  margin: 4rem;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

#conversation-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow-y: auto;
}

.question, .ai_response {
  padding: 1rem;
  width: 75%;
  line-height: 1rem;
  border-radius: 1.5rem;
  margin-bottom: 1rem;
  width: fit-content;
  min-width: 4rem;
}
.question {
  background-color: black;
  margin-left: auto;
}

.ai_response {
  background-color: #028;
  margin-right: auto;
}

.input-field {
  background-color: var(--color-background-mute);
  color: var(--color-text);
  font-size: 1rem;
  width: 100%;
  padding: 1rem;
  border: 0;
  border-radius: 1.5rem;
}
.input-field:focus {
  outline: none;
}

@media (max-width: 1024px) {
  #input-main {
    margin: 0;
    height: 100%;
  }
}

</style>