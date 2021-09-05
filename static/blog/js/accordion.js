
var jq = $.noConflict();

jq(document).ready(function() {
  jq('.collapse.in').prev('.panel-heading').addClass('active');
  jq('#accordion, #bs-collapse')
    .on('show.bs.collapse', function(a) {
      jq(a.target).prev('.panel-heading').addClass('active');
    })
    .on('hide.bs.collapse', function(a) {
      jq(a.target).prev('.panel-heading').removeClass('active');
    });
});
