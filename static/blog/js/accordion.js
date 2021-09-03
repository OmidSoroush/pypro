
var jq = $.noConflict();

jq('.i-accordion').on('show.bs.collapse', function(n){
  jq(n.target).siblings('.panel-heading').find('.panel-title i').toggleClass('fa-chevron-down fa-chevron-up');
});
jq('.i-accordion').on('hide.bs.collapse', function(n){
  jq(n.target).siblings('.panel-heading').find('.panel-title i').toggleClass('fa-chevron-up fa-chevron-down');
});

/* P */
jq('.accordion-2a, .accordion-2b, .accordion-3').on('show.bs.collapse', function(n){
  jq(n.target).siblings('.panel-heading').find('.panel-title i').toggleClass('fa-minus fa-plus');
});
jq('.accordion-2a, .accordion-2b, .accordion-3').on('hide.bs.collapse', function(n){
  jq(n.target).siblings('.panel-heading').find('.panel-title i').toggleClass('fa-plus fa-minus');
});
