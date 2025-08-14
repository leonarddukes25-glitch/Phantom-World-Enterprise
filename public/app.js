(function(){
  const leoBtn = document.getElementById('leoBtn');
  const leoPanel = document.getElementById('leoPanel');
  const leoClose = document.getElementById('leoClose');

  function openLeo(){ if(leoPanel){ leoPanel.classList.add('open'); leoPanel.setAttribute('aria-hidden','false'); } }
  function closeLeo(){ if(leoPanel){ leoPanel.classList.remove('open'); leoPanel.setAttribute('aria-hidden','true'); } }

  if (leoBtn) leoBtn.addEventListener('click', openLeo);
  if (leoClose) leoClose.addEventListener('click', closeLeo);
  if (leoPanel) leoPanel.addEventListener('click', (e)=>{ if(e.target===leoPanel) closeLeo(); });
  document.addEventListener('keydown', (e)=>{ if(e.key==='Escape') closeLeo(); });

  // highlight active nav link
  const here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a').forEach(a=>{
    if(a.getAttribute('href')===here) a.classList.add('active');
  });
})();
