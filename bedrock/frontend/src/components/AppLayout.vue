<template>
  <v-app>
    <NavBar />
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
      <div style="height: 500px"></div>
      <Footer />
    </v-main>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar';
import Footer from '@/components/Footer';

export default {
  name: 'AppLayout',
  components: {
    NavBar,
    Footer,
  },
};
</script>

<style></style>
