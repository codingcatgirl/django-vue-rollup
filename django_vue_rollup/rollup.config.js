import vue from 'rollup-plugin-vue';

export default {
  output: {
    format: 'iife',
    exports: 'named',
  },
  plugins: [
    vue({
      css: true,
      compileTemplate: true,
      needMap: false,
    }),
  ],
};
