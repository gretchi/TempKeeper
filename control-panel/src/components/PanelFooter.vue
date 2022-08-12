<template>
  <div class="row">
    <div class="col-2 col-parent">
      <button class="button el bg-magenta">メイン<br />メニュ</button>
    </div>

    <div class="col-2 col-parent">
      <button class="button el bg-yellow">主ヒータ制御</button>
    </div>

    <div class="col-2 col-parent"></div>

    <div class="col-2 col-parent">
      <button class="button el">ノード管理</button>
    </div>

    <div class="col-2 col-parent">
      <button class="button el">ネットワーク管理</button>
    </div>
    <div class="col-2 col-parent"></div>
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
