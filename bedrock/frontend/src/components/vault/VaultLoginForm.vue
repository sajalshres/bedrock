<template>
  <v-row>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultLogin.name"
        label="Name*"
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
        :items="['production', 'version', 'dev']"
        label="Labels"
        chips
        multiple
      ></v-autocomplete>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: {
    vaultLogin: {
      type: Object,
      default: () => ({
        name: '',
        type: '',
        username: '',
        password: '',
        link: '',
        labels: [],
      }),
    },
  },
  data: () => ({
    showPassword: false,
  }),
};
</script>

<style></style>
