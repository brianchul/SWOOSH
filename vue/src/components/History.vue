<template>
    <div>
        <div class= 'title'>Launch History</div>
        <div class= 'separate'></div>
        <div class= 'wrapper'>
            <div class= 'flex_row'>
                <img class='titleImg' src='../assets/white.png'/>
                <div class= 'subtitle'>Select Year : </div>
                <input class='input' v-model="year" @change="hello"/>
                <div class= "dropdown">
                    <div class= "dropbtn center"  @click="openContent=true">
                        <div class='triangle'></div>
                    </div>
                    <div class= "dropdown-content" :class="(openContent) ? 'open' : 'close'">
                        <div v-for="n in 15 " :key="n+2003" @click='itemClick(n)'>{{ n+2003 }}</div>
                    </div>
                </div> 
            </div>
        </div>
        <div class= "wrapper">
            <el-table 
                class="table" 
                :data="filterJson" 
                :default-sort = "{prop: 'launch_day', order: 'descending'}" 
                style="width: 80%" 
                height="450" >
                <el-table-column type="expand">
                    <template slot-scope="props">
                        <p>Purpose : {{ props.row.mission_discription }}</p>
                    </template>
                </el-table-column>
                <el-table-column 
                    :span="4"
                    prop="launch_day" 
                    width= "250" 
                    label="Launch Day"
                    align= "center"
                    sortable></el-table-column>
                <el-table-column 
                    prop="rocket_name" 
                    label="Name" 
                    width= "150" 
                    align= "left"></el-table-column>
                <el-table-column 
                    prop="launch_location"
                    label="Launch Location" 
                    align= "left"
                    ></el-table-column>
            </el-table>
        </div>
    </div>
    

</template>

<script>
import _ from 'lodash'
import json from '../lib/timeline.json'
export default {
    name: 'History',
    data() {
        return {
            openContent: false,
            year: 2018,
            initJson: json,
            filterJson: null,

        }
    },
    created() {
        this.initJson = _.orderBy(this.initJson, ['launch_day'], ['asc']);
        this.filterJson = this.initJson;
    },
    methods: {
        itemClick: function(n) {
            this.openContent = false;
            this.year = n+2003;
            var targetYear = this.year;

            this.filterJson = _.filter(this.initJson,function(payload) {
                return (payload.launch_day.match(/.{1,4}/g)[0] === targetYear.toString());
            });
        },
        hello: function(){
            var targetYear = this.year;
            this.filterJson = _.filter(this.initJson,function(payload) {
                return (payload.launch_day.match(/.{1,4}/g)[0] === targetYear.toString())
            });
        },
    },
    
}
</script>

<style scoped>
.title {
    color: #fff;
    font-size: 40px;
    font-family: sans-serif;
    border-bottom: 2px solid #fff;
    padding-bottom: 10px;
}
.subtitle {
    color: #fff;
    font-size: 20px;
    padding: 10px;
}
.titleImg{
    height: 40px;
}
.year {
    color: #000;
    font-size: 20px;
    font-family: sans-serif;
    padding: 10px;
}
.dropbtn {
    width: 20px;
    height: 20px;
    color: #000;
    cursor: pointer;
    padding: 5px;
    border-top: 2px solid transparent;
    border-bottom: 2px solid #fff;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
    position: relative;
    display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
    cursor: pointer;
    height: 200px;
    overflow: scroll;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}
.open {
    display: block;
}
.close {
    display: none;
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

.padding_right {
    padding-right: 2px;
}

.input {
    width: 50px;
    height: 10px;
    padding: 10px;
    background-color: rgba(0,0,0,0);
    border-left: 2px solid transparent;
    border-right: 2px solid transparent;
    border-top: 2px solid transparent;
    border-bottom: 2px solid #fff;
    font-size: 18px;
    color: #fff;
    text-align: center;
}

.flex_row {
    display: flex;
    flex-direction: row;
    padding: 5px;
    border-bottom: 2px solid #fff;
}

.inputWrapper {
    position: absolute;
    width:100px; 
    height:80px;

}
.triangle {
    width: 0; 
    height: 0; 
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 10px solid #fff;
}
.separate {
    width: 100%;
    height: 5px;
    border-bottom: 2px solid #fff;
}
.wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #fff;
    font-size: 18px;
    margin-top: 10px;
}
.table {
    border-radius: 10px;
}


</style>