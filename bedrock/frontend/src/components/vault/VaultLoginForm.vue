<template>
  <v-row>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultLogin.title"
        label="Title*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" sm="6" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultLogin.username"
        label="Username*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" sm="6" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultLogin.password"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        label="Password*"
        :type="showPassword ? 'text' : 'password'"
        required
        @click:append="showPassword = !showPassword"
      ></v-text-field>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultLogin.link"
        label="Link*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-textarea
        v-model="vaultLogin.note"
        counter
        rows="3"
        label="Notes"
      ></v-textarea>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-autocomplete
        v-model="vaultLogin.labels"
        :items="getLabelNames"
        label="Labels"
        chips
        multiple
      ></v-autocomplete>
    </v-col>
  </v-row>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  props: {
    vaultLogin: {
      type: Object,
      default: () => ({
        title: '',
        username: '',
        password: '',
        link: '',
        note: '',
        labels: [],
        type: '',
      }),
    },
  },
  data: () => ({
    showPassword: false,
  }),
  computed: {
    getLabelNames() {
      return this.getLabels.map(({ name }) => name);
    },
    ...mapGetters(['getLabels']),
  },
};
</script>

<style></style>
