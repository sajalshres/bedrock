<template>
  <v-dialog v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn class="mx-2" depressed fab small v-on="on">
        <v-icon dark>mdi-label-multiple</v-icon>
      </v-btn>
    </template>

    <v-card>
      <v-card-title>
        Labels
      </v-card-title>
      <v-card-text>
        <v-row no-gutters justify="center">
          <v-chip class="ma-1" label v-for="label in getLabels" :key="label.id">
            {{ label.name }}
          </v-chip>
        </v-row>
      </v-card-text>
      <v-card-text>
        <v-row v-if="isAuthenticated">
          <v-text-field
            flat
            solo-inverted
            hide-details
            append-icon="mdi-label"
            v-model="label"
            label="Add New Label"
            required
          ></v-text-field>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn depressed @click="dialog = false">Close</v-btn>
        <v-btn depressed @click="save">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
import { CREATE_RESOURCE } from '../store/actions.type';
export default {
  name: 'Labels',
  data: () => ({
    label: '',
    dialog: false,
  }),
  computed: {
    ...mapGetters(['isAuthenticated', 'getLabels']),
  },
  methods: {
    save() {
      console.log(this.label);
      this.createResource({
        type: 'labels',
        resource: {
          name: this.label,
        },
      });
      this.dialog = false;
    },
    ...mapActions({
      createResource: CREATE_RESOURCE,
    }),
  },
};
</script>

<style></style>
