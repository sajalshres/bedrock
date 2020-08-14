<template>
  <v-row>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultNote.title"
        label="Title*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-textarea
        v-model="vaultNote.note"
        counter
        rows="3"
        label="Notes*"
      ></v-textarea>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-autocomplete
        v-model="vaultNote.labels"
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
    vaultNote: {
      type: Object,
      default: () => ({
        title: '',
        note: '',
        labels: [],
        type: '',
      }),
    },
  },
};
</script>

<style></style>
