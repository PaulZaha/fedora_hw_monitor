<template>
  <div>
    <h1>Systemstatistiken CPU</h1>
    <div>
      <p>CPU Usage: {{ cpu_data.usage }}%</p>
      <p>CPU Frequency: {{ cpu_data.freq }} MHz</p>
      <p>CPU Temperature: {{ cpu_data.temp }}°C</p>
    </div>
    <h1>Systemstatistiken GPU</h1>
    <div>
      <p>GPU Usage: {{ gpu_data.usage }}%</p>
      <p>GPU Memory Usage: {{ gpu_data.mem_usage }}%</p>
      <p>GPU Temp: {{ gpu_data.temp }}°C</p>

    </div>

    <h1>Update-Intervall</h1>
    <input type="number" v-model="intervalinput">
    <button @click="update">Update</button>

    
  </div>
</template>

<script>
import Axios from 'axios';

export default {
  data() {
    return {
      cpu_data: {
        usage: null,
        freq: null,
        temp: null,
      },
      gpu_data: {
        usage: null,
        mem_usage: null,
        temp: null,
      },
      intervalinput: null,
      interval: 2000, // Default-Intervall in ms
      intervalId: null,

    };
  },
  mounted() {
    this.get_cpu_data();
    this.intervalId = setInterval(this.get_cpu_data, this.interval);
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
  methods: {
    update() {
      clearInterval(this.intervalId);
      this.interval = this.intervalinput * 1000;
      this.intervalId = setInterval(this.get_cpu_data, this.interval);
      console.log(this.interval);
    },
    async get_cpu_data() {
      try {
        const response = await Axios.get('http://127.0.0.1:5000/stats');
        this.cpu_data.usage = response.data.cpu_data.usage;
        this.cpu_data.freq = response.data.cpu_data.freq;
        this.cpu_data.temp = response.data.cpu_data.temp;
        this.gpu_data.usage = response.data.gpu_util;
        this.gpu_data.temp = response.data.gpu_temp;
        this.gpu_data.mem_usage = response.data.gpu_mem_util;

        const currentTime = Date.now();

      } catch (error) {
        console.error('Fehler beim Abrufen der CPU-Daten:', error);
        this.cpu_data.usage = 0;
        this.cpu_data.freq = 0;
        this.cpu_data.temp = 0;
      }
    },
  },
};
</script>

<style scoped>
p {
  font-size: 1.2rem;
}
</style>
