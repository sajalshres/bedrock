<template>
  <v-dialog v-model="dialog" persistent max-width="600px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn class="mx-2" depressed fab small v-on="on" v-bind="attrs">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <span class="headline">New Vault Item</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" class="ma-0 pa-1">
              <v-select
                @change="updateVaultTypeForm"
                v-model="vaultType"
                :items="vaultTypes"
                label="What type of vault item is this?"
              ></v-select>
            </v-col>
          </v-row>
          <VaultItemForm v-if="vaultType === 'Vault Item'" />
          <VaultLoginForm v-else-if="vaultType === 'Vault Login'" />
          <VaultNoteForm v-else-if="vaultType === 'Vault Note'" />
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
        <v-btn color="blue darken-1" text @click="save">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import VaultItemForm from './VaultItemForm';
import VaultLoginForm from './VaultLoginForm';
import VaultNoteForm from './VaultNoteForm';
export default {
  components: {
    VaultItemForm,
    VaultLoginForm,
    VaultNoteForm,
  },
  data: () => ({
    dialog: false,
    vaultType: 'Vault Item',
    vaultTypes: ['Vault Item', 'Vault Login', 'Vault Note'],
  }),
  methods: {
    save() {},
    updateVaultTypeForm(vaultType) {
      this.vaultType = vaultType;
    },
  },
};
</script>

<style></style>
