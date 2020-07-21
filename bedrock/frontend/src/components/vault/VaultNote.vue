<template>
  <v-row>
    <v-dialog v-model="dialog" max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn text v-bind="attrs" v-on="on">
          <v-icon left>mdi-note-text</v-icon>
          {{ vaultNote.name }}
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Edit: {{ vaultNote.name }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model="vaultNote.name"
                  label="Name*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-autocomplete
                  :items="[
                    'Skiing',
                    'Ice hockey',
                    'Soccer',
                    'Basketball',
                    'Hockey',
                    'Reading',
                    'Writing',
                    'Coding',
                    'Basejump',
                  ]"
                  label="Labels"
                  multiple
                ></v-autocomplete>
              </v-col>
              <v-col cols="12">
                <v-textarea label="Notes"></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false"
            >Close</v-btn
          >
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  props: {
    vaultNote: Object,
  },
  data: () => ({
    data: false,
    dialog: false,
  }),
};
</script>

<style></style>
