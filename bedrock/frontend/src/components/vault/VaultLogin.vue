<template>
  <v-row>
    <v-dialog v-model="dialog" max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn text v-bind="attrs" v-on="on">
          <v-icon left>mdi-key-variant</v-icon>
          {{ vaultLogin.name }}
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Edit: {{ vaultLogin.name }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
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
                  multiple
                ></v-autocomplete>
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
    vaultLogin: Object,
  },
  data: () => ({
    data: false,
    dialog: false,
    showPassword: false,
  }),
};
</script>

<style></style>
