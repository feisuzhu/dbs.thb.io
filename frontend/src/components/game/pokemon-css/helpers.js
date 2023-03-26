import { ref, reactive } from 'vue';

export const activeCard = ref(null);

const getRawOrientation = function(e) {
  if ( !e ) {
    return { alpha: 0, beta: 0, gamma: 0 };
  } else {
    return { alpha: e.alpha, beta: e.beta, gamma: e.gamma };
  }
}

const getOrientationObject = (e) => {
  const orientation = getRawOrientation(e);
  return {
    absolute: orientation,
    relative: {
      alpha: orientation.alpha - baseOrientation.alpha,
      beta: orientation.beta - baseOrientation.beta,
      gamma: orientation.gamma - baseOrientation.gamma,
    }
  }
}

let firstReading = true;
let baseOrientation = getRawOrientation();

export const resetBaseOrientation = () => {
  firstReading = true;
  baseOrientation = getRawOrientation();
}

export const orientation = reactive(getOrientationObject());

// https://developer.mozilla.org/en-US/docs/Web/API/Window/ondeviceorientation
const handleOrientation = function(e) {

  if ( firstReading ) {
    firstReading = false;
    baseOrientation = getRawOrientation(e);
  }

  const o = getOrientationObject(e);
  Object.assign(orientation, o);
};

window.addEventListener("deviceorientation", handleOrientation, true);


export const round = (value, precision = 3) => parseFloat(value.toFixed(precision));
export const clamp = (value, min = 0, max = 100 ) => {
	return Math.min(Math.max(value, min), max);
};
export const adjust = (value, fromMin, fromMax, toMin, toMax) => {
	return round(toMin + (toMax - toMin) * (value - fromMin) / (fromMax - fromMin));
};

function dec2hex (dec) {
  return dec.toString(16).padStart(2, "0")
}

export const generateId = len => {
  var arr = new Uint8Array((len || 40) / 2)
  window.crypto.getRandomValues(arr)
  return Array.from(arr, dec2hex).join('')
}
