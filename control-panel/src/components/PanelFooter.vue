<template>
  <div class="row">
    <div class="col col-parent">
      <button class="button el bg-magenta">主ヒータ制御</button>
    </div>
    <div class="col col-parent">
      <button class="button el bg-yellow">ノード管理</button>
    </div>

    <div class="col col-parent"></div>

    <div class="col col-parent">
      <button class="button el bg-green">疎通正常</button>
    </div>
    <div class="col col-parent">
      <button class="button el bg-green">温度正常</button>
    </div>

    <div class="col col-parent"></div>
  </div>
</template>

<script>
export default {
  props: {},
  data: function () {
    return {};
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
