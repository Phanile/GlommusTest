<template>
  <div class="app">
    <div class="nav" v-if="additionally">
      <h1>Main App</h1>
      <router-link to="/about">About</router-link>
      <router-link to="/">Home</router-link>
    </div>
    <router-view v-if="additionally"/>

    <div class="table">
      <h1>Players table</h1>
      <table>
        <thead>
          <tr>
            <th>id</th>
            <th>name</th>
            <th>money</th>
            <th>gems</th>
            <th>level</th>
            <th>damage</th>
            <th>friends</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="player in players" :key="player.id">
            <td class="id">{{ player.id }}</td>
            <td>{{ player.name }}</td>
            <td>{{ player.money }}</td>
            <td>{{ player.gems }}</td>
            <td>{{ player.level }}</td>
            <td>{{ player.damage }}</td>
            <td>{{ player.friends }}</td>
          </tr>
        </tbody>
      </table>

      <div class="add">
        <h2>New player</h2>
        <input type="text" placeholder="name" v-model="currentPlayer.name">
        <input type="text" placeholder="money" v-model.number="currentPlayer.money">
        <input type="text" placeholder="gems" v-model.number="currentPlayer.gems">
        <input type="text" placeholder="level" v-model.number="currentPlayer.level">
        <input type="text" placeholder="damage" v-model.number="currentPlayer.damage">
        <input type="text" placeholder="friends" v-model="currentPlayer.friends">
        <button>Add player</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',

  data(){
    return{
      additionally: true,
      players: [],
      currentPlayer: {}
    }
  },

  async created(){
    const response = await fetch('http://127.0.0.1:8000/api/players/')
    this.players = await response.json()
  }
}
</script>

<style lang="scss">
  $maincolor: #41b883;

  *{
    color: rgba(0,0,0,.8);
    font-family: Roboto;
    font-weight: 400;
  }

  .app{
    text-align: center;
    margin-top: 20px;

    .nav{
      margin-bottom: 25px;
    }

    h1{
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      color: rgba(0,0,0,.8);
      margin-bottom: 10px;
    }

    a{
      font-size: 18px;
      padding: 8px;
      color: $maincolor
    }
  }

  .table{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-top: 50px;

    table{
      th, td{
        padding: 4px;
      }
      
      th, .id{
        font-weight: 500;
      }
    }

    .add{
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2px;
      border: 1px solid rgba(0,0,0,.4);
      border-radius: 2px;
      margin-top: 20px;

      h2{
        margin-bottom: 5px;
      }

      input{
        padding: 5px;
      }

      button{
        width: 60%;
        padding: 5px;
        background-color: $maincolor;
        color: white;
        border-radius: 2px;
        margin-top: 10px;
      }
    }
  }
    
</style>
