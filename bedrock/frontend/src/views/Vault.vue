<template>
  <v-container fluid>
    <BreadCrumbs />
    <v-data-table
      :headers="headers"
      :items="vault"
      :search="search"
      :dense="dense"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar flat class="pt-2">
          <v-text-field
            v-model="search"
            prepend-inner-icon="mdi-magnify"
            label="Search"
            clearable
            hide-details
            class="pb-1"
          ></v-text-field>
          <v-spacer />
          <VaultCreate />
          <v-btn class="mx-2" depressed fab small @click.stop>
            <v-icon dark>mdi-reload</v-icon>
          </v-btn>
          <v-switch class="mx-2 pt-4" label="Small" v-model="dense"></v-switch>
        </v-toolbar>
      </template>
      <template v-slot:item.name="{ item }">
        <VaultEdit :vaultRecord="item" />
      </template>
      <template v-slot:item.labels="{ item }">
        <v-chip
          label
          small
          class="ml-2 my-2"
          v-for="label in item.labels"
          :key="label"
          >{{ label }}</v-chip
        >
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import BreadCrumbs from '../components/BreadCrumbs';
import VaultEdit from '../components/vault/VaultEdit';
import VaultCreate from '../components/vault/VaultCreate';

export default {
  name: 'Vault',
  components: {
    BreadCrumbs,
    VaultEdit,
    VaultCreate,
  },
  data: () => ({
    resourceType: 'vault',
    loadingText: 'Loading vault, please wait.',
    fab: false,
    dense: false,
    dialog: false,
    expanded: [],
    singleExpand: true,
    search: '',
    headers: [
      { text: 'Name', value: 'name', align: 'start', width: '40%' },
      { text: 'Type', value: 'type', align: 'end' },
      { text: 'Labels', value: 'labels', align: 'end' },
    ],
  }),
  created() {
    this.initialize();
  },
  methods: {
    initialize() {
      this.vault = [
        {
          name: 'Bedrock Version',
          type: 'item',
          value: '0.1',
          labels: ['production', 'version'],
        },
        {
          name: 'Bedrock CLI Version',
          type: 'item',
          value: '0.1',
          labels: ['production', 'version'],
        },
        {
          name: 'Github',
          type: 'login',
          username: 'testUser',
          password: 'da3132321!#$',
          link: 'https://www.github.com',
          labels: ['dev'],
        },
        {
          name: 'Github SSH KEY',
          type: 'note',
          note: 'kasdjsakldjlkdjaksljdq9249274239021-02323@!#*@)($&*@)(',
          labels: ['dev'],
        },
      ];
    },
  },
};
</script>

<style></style>
