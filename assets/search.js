(function(){
  async function load() {
    try {
      const res = await fetch('data.json');
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const items = await res.json();
      const container = document.getElementById('list');
      container.innerHTML = '';
      items.forEach(it => {
        const d = document.createElement('div');
        d.className = 'item';
        const catStr = (it.categories || []).join(', ');
        const deplStr = (it.deployment || []).join(', ');
        const intStr = (it.interfaces || []).join(', ');
        const techStr = (it.technical ? `${it.technical.language || '-'} / ${it.technical.database || '-'}` : '-');
        d.innerHTML = `<strong><a href="${it.link}" target="_blank" rel="noopener">${it.name}</a></strong>
          <div>${it.description || ''}</div>
          <table style="margin-top:0.5rem;width:100%;border-collapse:collapse;">
            <tr><td style="width:150px;"><em>Provider:</em></td><td>${it.provider || '-'}</td></tr>
            <tr><td><em>Categories:</em></td><td>${catStr || '-'}</td></tr>
            <tr><td><em>License:</em></td><td>${it.license || '-'}</td></tr>
            <tr><td><em>Open Source:</em></td><td>${it.open_source ? 'Yes' : 'No'}</td></tr>
            <tr><td><em>Deployment:</em></td><td>${deplStr || '-'}</td></tr>
            <tr><td><em>Tech Stack:</em></td><td>${techStr}</td></tr>
            <tr><td><em>Interfaces:</em></td><td>${intStr || '-'}</td></tr>
          </table>`;
        container.appendChild(d);
      });
    } catch (err) {
      const c = document.getElementById('list');
      c.textContent = 'Error loading data: ' + err;
    }
  }
  window.addEventListener('DOMContentLoaded', load);
})();
async function loadData(){
  try{
    const r = await fetch('data.json');
    const data = await r.json();
    const el = document.getElementById('list');
    if(!data.length) el.textContent = 'Keine Einträge.';
    el.innerHTML = '';
    data.forEach(d=>{
      const div = document.createElement('div');
      div.className = 'item';
      div.innerHTML = `<strong>${d.name}</strong> — ${d.description || ''} <br><a href="${d.website}">${d.website}</a>`;
      el.appendChild(div);
    })
  }catch(e){
    document.getElementById('list').textContent = 'Fehler beim Laden der Daten.';
    console.error(e);
  }
}
loadData();
