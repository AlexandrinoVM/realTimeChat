function parseJwt(token) {
    try {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split('')
          .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
          .join('')
      );
      return JSON.parse(jsonPayload);
    } catch (e) {
      console.error('Token inválido:', e);
      return null;
    }
  }

  const token = localStorage.getItem('access_token');

  if (!token) {
    window.location.href = 'login.html';
  } else {
    const payload = parseJwt(token);
    if (payload) {
      document.getElementById('username').textContent = payload.username || payload.sub || 'Usuário';
    } else {
      alert('Token inválido!');
      localStorage.removeItem('access_token');
      window.location.href = 'login.html';
    }
  }

  function logout() {
    localStorage.removeItem('access_token');
    window.location.href = 'index.html';
  }
  var globalRoom

  async function fetchRooms(token) {
    try {
      const res = await fetch('http://127.0.0.1:8000/room/get', {
        //eaders: {
          //'Authorization': `Bearer ${token}`
        //}
      });
      const rooms = await res.json();
      const list = document.getElementById('room-list');
      rooms.forEach(room => {
        const li = document.createElement('li');
        li.textContent = room.name;
        li.onclick = () => {
          userModal()
          globalRoom = room.id
          //window.location.href = `chat.html?id=${room.id}`
        };
        list.appendChild(li);
      });
    } catch (err) {
      console.error('Erro ao buscar salas:', err);
      alert('Erro ao carregar as salas.');
    }
  }

  function openModal() {
    document.getElementById('modal').style.display = 'flex';
  }

  function closeModal() {
    document.getElementById('modal').style.display = 'none';
  }

  function closeModal_select(){
    document.getElementById('modal_select').style.display = 'none';
  }

  function gotoRoom(){
    window.location.href = `chat.html?id=${globalRoom}`
    closeModal_select()
  }

  async function deleteRoom(){
      const res = await fetch(`http://127.0.0.1:8000/room/delete/${globalRoom}`,{
        method: 'DELETE'
      })
      const resp = await res.json()
      console.log(resp)
      document.getElementById('room-list').innerHTML = "";
      fetchRooms(token)
      closeModal_select()
  }

  function userModal() {
    document.getElementById('modal_select').style.display = 'flex';
  }

  async function createRoom(){
    var name = document.getElementById('new-room-name').value
    try {
      const res = await fetch('http://127.0.0.1:8000/room/create', {
        method: "POST",
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name:name})
      });
      document.getElementById('room-list').innerHTML = "";
      fetchRooms(token)
    } catch (err) {
      console.error('Erro ao buscar salas:', err);
      alert('Erro ao carregar as salas.');
    }
  }


  document.addEventListener('DOMContentLoaded', fetchRooms);