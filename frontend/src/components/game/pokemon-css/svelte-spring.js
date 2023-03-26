import { reactive } from 'vue';

function tick_spring(ctx, last_value, current_value, target_value) {
  if (typeof current_value === 'number') {
    const delta = target_value - current_value;
    const velocity = (current_value - last_value) / (ctx.dt || 1 / 60); // guard div by 0
    const spring = ctx.opts.stiffness * delta;
    const damper = ctx.opts.damping * velocity;
    const acceleration = (spring - damper) * ctx.inv_mass;
    const d = (velocity + acceleration) * ctx.dt;
    if (Math.abs(d) < ctx.opts.precision && Math.abs(delta) < ctx.opts.precision) {
      return target_value; // settled
    }
    else {
      ctx.settled = false; // signal loop to keep ticking
      return current_value + d;
    }
  }
  else if (Array.isArray(current_value)) {
    return current_value.map((_, i) => tick_spring(ctx, last_value[i], current_value[i], target_value[i]));
  }
  else if (typeof current_value === 'object') {
    const next_value = {};
    for (const k in current_value) {
      next_value[k] = tick_spring(ctx, last_value[k], current_value[k], target_value[k]);
    }
    return next_value;
  }
  else {
    throw new Error(`Cannot spring ${typeof current_value} values`);
  }
}

export function spring(value, opts = {}) {
  const calculated = reactive(value);
  const { stiffness = 0.15, damping = 0.8, precision = 0.01 } = opts;
  let last_time;
  let task;
  let last_value = value;
  let target_value = value;
  let next_value = value;
  let inv_mass = 1;
  let inv_mass_recovery_rate = 0;
  let cancel_task = false;

  function tick(now) {
    if (cancel_task) {
      cancel_task = false;
      task = null;
      return;
    }
    inv_mass = Math.min(inv_mass + inv_mass_recovery_rate, 1);
    const ctx = {
      inv_mass,
      opts: spring,
      settled: true,
      dt: (now - last_time) * 60 / 1000
    };
    next_value = tick_spring(ctx, last_value, value, target_value);
    last_time = now;
    last_value = value;
    value = next_value;
    Object.assign(calculated, value);
    if (ctx.settled) {
      task = null;
    } else {
      task = requestAnimationFrame(tick);
    }
  }

  function set(new_value, opts = {}) {
    target_value = new_value;
    if (value == null || opts.hard || (spring.stiffness >= 1 && spring.damping >= 1)) {
      cancel_task = true; // cancel any running animation
      last_time = window.performance.now();
      last_value = new_value;
      value = next_value;
      Object.assign(calculated, value);
      return;
    }
    else if (opts.soft) {
      const rate = opts.soft === true ? .5 : +opts.soft;
      inv_mass_recovery_rate = 1 / (rate * 60);
      inv_mass = 0; // infinite mass, unaffected by spring forces
    }
    if (!task) {
      last_time = window.performance.now();
      cancel_task = false;
      task = requestAnimationFrame(tick);
    }
  }

  const spring = {
    set,
    update: (fn, opts) => set(fn(target_value, value), opts),
    values: calculated,
    stiffness,
    damping,
    precision
  };
  return spring;
}
