<template>
  <v-row>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn text v-bind="attrs" v-on="on">
          <v-icon left>{{ getVaultIcon() }}</v-icon>
          {{ vaultRecord.name }}
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Edit: {{ vaultRecord.name }}</span>
        </v-card-title>
        <v-card-text>
          <VaultItemForm
            :vaultItem="vaultRecord"
            v-if="vaultRecord.type === 'item'"
          />
          <vaultLoginForm
            :vaultLogin="vaultRecord"
            v-else-if="vaultRecord.type === 'login'"
          />
          <vaultNoteForm
            :vaultNote="vaultRecord"
            v-else-if="vaultRecord.type === 'note'"
          />
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false"
            >Close</v-btn
          >
          <v-btn color="blue darken-1" text @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import VaultItemForm from './VaultItemForm';
import vaultLoginForm from './vaultLoginForm';
import vaultNoteForm from './vaultNoteForm';
export default {
  components: {
    VaultItemForm,
    vaultLoginForm,
    vaultNoteForm,
  },
  props: {
    vaultRecord: Object,
  },
  data: () => ({
    data: false,
    dialog: false,
  }),
  methods: {
    save() {
      console.log({ vaultRecord: this.vaultRecord });
      this.dialog = false;
    },
    getVaultIcon() {
      return {
        item: 'mdi-contain',
        login: 'mdi-key-variant',
        note: 'mdi-notebook',
      }[this.vaultRecord.type];
    },
  },
};
</script>

<style></style>
