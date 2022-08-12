<template>
  <div class="row">
    <div class="col col-parent">
      <p class="h5 bg-yellow">{{ title }}</p>
      <p class="h5 bg-cyan">{{ calendar }} {{ clock }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
  },
  data: function () {
    return {
      calendar: "",
      clock: "",
    };
  },
  methods: {
    updateClock: function () {
      const date = new Date();
      const days = ["日", "月", "火", "水", "木", "金", "土"];
      this.calendar =
        date.getFullYear() +
        "/" +
        (date.getMonth() + 1) +
        "/" +
        date.getDate() +
        "(" +
        days[date.getDay()] +
        ")";
      this.clock =
        date.getHours() +
        ":" +
        ("00" + date.getMinutes()).slice(-2) +
        ":" +
        ("00" + date.getSeconds()).slice(-2);
    },
  },
  mounted: function () {
    // run once
    this.updateClock();

    // timer interrupt
    setInterval(() => {
      this.updateClock();
    }, 500);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
