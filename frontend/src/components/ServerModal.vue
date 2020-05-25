<template>
  <v-dialog v-model="dialog" width="400">
    <template v-slot:activator="{ on }">
      <v-btn
        class="mx-1"
        :color="getStatusColor(server.status)"
        rounded
        small
        dark
        v-on="on"
      >
        {{ server.name }}
      </v-btn>
    </template>

    <v-card class="mx-auto" outlined>
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">Server Details</div>
          <v-list-item-title class="headline mb-1 text-uppercase">{{
            server.name
          }}</v-list-item-title>
          <v-list-item-subtitle v-if="hasLabels">
            <v-chip
              x-small
              class="mr-1"
              color="orange lighten-3"
              v-for="label in server.labels"
              :key="label"
              >{{ label }}</v-chip
            >
          </v-list-item-subtitle>
          <v-list-item-subtitle v-else>
            <v-chip x-small class="mr-1" color="orange lighten-3"
              >No Labels</v-chip
            >
          </v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-avatar tile size="80">
          <v-icon size="80" :color="getStatusColor(server.status)"
            >mdi-server</v-icon
          >
        </v-list-item-avatar>
      </v-list-item>
      <v-card-text>
        <v-row no-gutters>
          <v-col cols="6">IP Address</v-col
          ><v-col>{{ server.ip_address }}</v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Category</v-col><v-col>{{ server.category }}</v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Owner</v-col><v-col>{{ server.owner }}</v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Domain</v-col><v-col>{{ server.domain }}</v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Cluster</v-col><v-col>{{ server.cluster }}</v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Environments</v-col
          ><v-col
            ><v-chip
              x-small
              label
              class="mr-1"
              v-for="environment in server.environments"
              :key="environment"
              >{{ environment }}</v-chip
            ></v-col
          >
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Status</v-col><v-col>{{ server.status }}</v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="6">Description</v-col
          ><v-col>{{ server.description }}</v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import { getStatusColor } from '../utils/common';
export default {
  props: {
    server: Object,
  },
  data: () => ({}),
  methods: {
    getStatusColor: getStatusColor,
  },
  computed: {
    dialog() {
      return false;
    },
    hasLabels() {
      return this.server.labels.length > 0;
    },
  },
};
</script>
