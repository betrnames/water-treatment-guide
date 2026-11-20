
(function(){
  var SIZES=[24000,32000,40000,48000,64000,80000,96000,110000];
  function $(id){return document.getElementById(id);}
  function fmt(n){return Math.round(n).toLocaleString('en-US');}
  function calc(){
    var h=parseFloat($('hard').value), unit=$('unit').value, fe=parseFloat($('iron').value)||0,
        ppl=parseFloat($('people').value), gpd=parseFloat($('gpd').value), days=parseFloat($('days').value);
    var out=$('out');
    if(!(h>=0)||!(ppl>0)||!(gpd>0)||!(days>0)){out.innerHTML='<p>Enter your hardness, household size, gallons per person, and days between regenerations.</p>';return;}
    var gpg = unit==='mgl' ? h/17.1 : h;
    var comp = gpg + 4*fe;
    var daily = comp*ppl*gpd;
    var need = daily*days;
    var pick=null; for(var i=0;i<SIZES.length;i++){ if(need<=SIZES[i]*0.75){pick=SIZES[i];break;} }
    var cls = gpg<1?'soft':gpg<3.5?'slightly hard':gpg<7?'moderately hard':gpg<10.5?'hard':'very hard';
    var html='<p class="big">'+fmt(need)+' grains</p><p>to remove between regenerations ('+days+' days).</p>'+
      '<ul><li>Your water: <strong>'+gpg.toFixed(1)+' gpg</strong> ('+cls+')'+(fe>0?', <strong>'+comp.toFixed(1)+' gpg</strong> after adding iron':'')+'</li>'+
      '<li>Daily load: '+fmt(comp)+' gpg × '+ppl+' people × '+gpd+' gal = <strong>'+fmt(daily)+' grains/day</strong></li>';
    if(pick){html+='<li>Rule-of-thumb size: <strong>'+(pick/1000)+',000-grain</strong> softener (your need is '+Math.round(need/pick*100)+'% of its rated capacity), about '+(pick/32000).toFixed(1)+' cu ft of resin</li>';}
    else{html+='<li>Your need is above common single-tank sizes. Shorten the days between regenerations, or ask about a larger or twin-tank system.</li>';}
    html+='</ul>';
    if(gpg<3.5){html+='<p class="small"><strong>Note:</strong> under 3.5 gpg is soft to slightly hard. Many homes at this level skip a softener entirely.</p>';}
    if(fe>0){html+='<p class="small"><strong>Iron:</strong> check the softener spec sheet for its iron limit. Higher iron usually means a dedicated iron filter first. See our well water guide.</p>';}
    out.innerHTML=html;
  }
  ['hard','unit','iron','people','gpd','days'].forEach(function(id){var el=$(id);el.addEventListener('input',calc);el.addEventListener('change',calc);});
  $('calc-form').addEventListener('submit',function(e){e.preventDefault();calc();});
  calc();
})();
