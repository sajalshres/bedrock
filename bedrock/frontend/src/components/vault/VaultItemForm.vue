<template>
  <v-row>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultItem.title"
        label="Title*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultItem.name"
        label="Name*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-text-field
        v-model="vaultItem.value"
        label="Value*"
        required
      ></v-text-field>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-textarea
        v-model="vaultItem.note"
        counter
        rows="3"
        label="Notes"
      ></v-textarea>
    </v-col>
    <v-col cols="12" class="ma-0 pa-1">
      <v-autocomplete
        v-model="vaultItem.labels"
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
    vaultItem: {
      type: Object,
      default: () => ({
        title: '',
        name: '',
        value: '',
        labels: [],
        type: '',
      }),
    },
  },
};
</script>

<style></style>
