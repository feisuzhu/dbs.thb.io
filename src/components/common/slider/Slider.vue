<template>
  <div class="slider">
      <ul>
          <slot />
      </ul>
  </div>
</template>

<style>
.slider {
  position: relative;
  margin: 0px auto;
  width: 100%;
  height: calc(100vw * 0.3635);
  min-height: 200px;
  background: #ccc;
}

.slider ul {
  margin: 0 0 0 0;
}

.slider ul li {
  position: absolute;
  background-repeat: no-repeat;
  background-size: cover;
  background-position:center;
  left: 0;
  top: 0;
  display: block;
  width: 100%;
  height: 100%;
  list-style: none;
}

.slider .dots {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 20px;
  width: 100%;
  z-index: 3;
  text-align: center;
}

.slider .dots li {
  display: inline-block;
  margin: 0 10px;
	width: 10px;
	height: 10px;
	border: 2px solid #fff;
	border-radius: 50%;
  opacity: 0.4;
	cursor: pointer;
	transition: background .5s, opacity .5s;
  list-style: none;
}

.slider .dots li.active {
  background: #fff;
	opacity: 1;
}

.slider .arrow {
  position: absolute;
  z-index: 2;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: background .5s, opacity .5s;
}

.slider .arrow .arrow-left,
.slider .arrow .arrow-right {
  position: absolute;
  top: 50%;
  margin-top: -25px;
  display: block;
  width: 50px;
  height: 50px;
  cursor: pointer;
  opacity: 0.5;
	transition: background .5s, opacity .5s;
}

.slider .arrow  .arrow-left:hover,
.slider .arrow  .arrow-right:hover {
  opacity: 1;
}

.slider .arrow .arrow-left {
  left: 20px;
  background: url("arrow-left.png");
}

.slider .arrow .arrow-right {
  right: 20px;
  background: url("arrow-right.png");
}
</style>

<script>
  import './slider.js';

  export default {
    name: 'slider',
    props: [
        'speed', 'show-arrow',
    ],
    mounted() {
      $(this.$el).slide({
          'slideSpeed': this.speed,
          'isShowArrow': this.showArrow,
          'dotsEvent': 'mouseenter',
          'isLoadAllImgs': true
      });
    },
  }
</script>
