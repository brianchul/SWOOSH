<template>
    <div>
        <div class='title'>Launch History</div>
        <div class='subtitle'>Select Year</div>
        

        <div class="dropdown">
            <button class="dropbtn">Dropdown</button>
            <div class="dropdown-content">
                <div v-for="n in 100 " :key="n+1910" @click='year = n+1910'>{{ n+1910 }}</div>
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    name: 'History',
    data() {
        return {
            year: 0,
        }
    },
}
</script>

<style scoped>
.title{
    color: #fff;
    font-size: 30px;
    font-family: sans-serif;
    border-bottom: 2px solid #fff;
    padding-bottom: 10px;
}
.subtitle{
    color: #000;
    font-size: 15px;
    font-family: sans-serif;
    padding: 10px;
}
.dropbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px;
    font-size: 16px;
    border: none;
    cursor: pointer;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: relative;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content div {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
}

.dropdown-content div:hover {
    background-color: #f1f1f1
}

.dropdown:hover .dropdown-content {
    display: block;
}

.dropdown:hover .dropbtn {
    background-color: #3e8e41;
}
 
</style>