<template>
    <div class='listWrapper'>
        <div class='listTitle'>
            <img class='titleIcon' src='../../assets/white.png'/>
            {{ listTitle }}
        </div>
        <div class='list'>
            <div class='row'>
                <div v-for='(value,key) in tags' :key='key' class='item'>
                    {{ value }}
                </div>
            </div>
            <div class='itemWrapper'>
                <div v-for='(item,index) in payload' :key='index'
                class='row' :class='(index%2 === 0) ? "even" : "" '>
                    <div v-for='(value,key) in item' :key='index+"-"+key' class='item'>
                        {{ value }}
                    </div>
                    <div class='buttonWrapper center'>
                        {{ buttonText }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'List',
    props: {
        listName: String,
        payload: Array,
    },
    data() {
        const { listName } = this
        return {
            listTitle: (listName === 'need') ? '需求清單' : '販售清單',
            buttonText: (listName === 'need') ? '聯絡' : '訂購',
            tags: (listName === 'need') ? {
                name: '名稱',
                weight: '重量',
                height: '高度',
                inclination: '傾角',
                launchDate: '發射日期',
            } : {
                launchDate: '發射日期',
                limitWeight: '限制重量',
                height: '高度',
                inclination: '傾角',
                price: '價格',
            },
        }
    },
    methods: {
        
    },
    created() {
    },
}
</script>

<style scoped>
.listWrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #fff;
    font-size: 18px;
    margin-top: 10px;
}
.listTitle {
    width: 95%;
    height: 50px;
    line-height: 50px;
}
.titleIcon {
    height: 38px;
}
.list {
    width: 95%;
    border-top: 2px solid #fff;
    border-bottom: 1px solid #fff;
}
.list .row {
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
    height: 50px;
    border-bottom: 1px solid #fff;
}
.list .row:hover .buttonWrapper {
    right: 20px;
}
.list .even {
    background-color: rgba(0,0,0,0.3);
}
.list .item {
    position: relative;
    width: calc((100% - 150px)/5);
    line-height: 50px;
    padding-left: 10px;
}
.itemWrapper {
    height: 255px;
    overflow-y: scroll;
    overflow-x: hidden;
}
.buttonTransition-enter-active, .buttonTransition-leave-active {
    transition: 
}
.buttonTransition-enter, .buttonTransition-leave-to {
    height: 0px;
}
.buttonWrapper {
    position: absolute;
    right: -100px;
    width: 80px;
    height: 30px;
    border: 2px solid #fff;
    border-radius: 15px;
    transition: right 1s;
}
.buttonWrapper:hover {
    border: 2px solid #000;
}
.buttonWrapper:hover .button{
    background-color: #000;
    color: #fff;
}
.sortButtonWrapper {
    display: flex;
}
.sortButton {
    width: 0px;
    height: 0px;
    border-style: solid;
    border-width: 10px 5px 0px 5px;
    border-color: #fff transparent transparent transparent;
    margin: 20px;
}
.item .down {
    border-width: 10px 5px 0px 5px;
    border-color: #fff transparent transparent transparent;
}
.item .up {
    border-width: 0px 5px 10px 5px;
    border-color: transparent transparent #fff transparent;
}
</style>