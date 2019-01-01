<template>
    <div class='listWrapper'>
        <div class='listTitle'>
            <img class='titleIcon' src='../../assets/white.png'/>
            {{ (listName === 'need') ? '需求清單' : '販售清單' }}
        </div>
        <div class='list'>
            <div class='row'>
                <div v-for='(value,key) in tags' :key='key' class='item'>
                    {{ value }}
                </div>
            </div>
            <div v-if='payload.length === 0' class='noData center'>目前無資料</div>
            <div v-else-if='modal' class='modal center'>
                <div class='close cross' @click='modal = false'></div>
                <div v-for='(value,key) in contactTags' :key='key'> {{value}}：{{itemInfo[key]}}</div>
                <div v-if='listName === "sale"'>
                    <div v-for='(value,key) in detailTags' :key='key'> {{value}}：{{detail[key]}}</div>
                </div>
            </div>
            <div v-else class='itemWrapper'>
                <div v-for='(item,index) in payload' :key='index'
                class='row' :class='(index%2 === 0) ? "even" : "" '>
                    <div v-for='(value,key) in tags' :key='index+"-"+key' class='item'>
                        {{ item[key] }}
                    </div>
                    <div class='buttonWrapper center' @click='getContact(item)'>
                        {{ (listName === 'need') ? '聯絡' : '訂購' }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import _ from 'lodash'
import api from '../../lib/'
export default {
    name: 'List',
    props: {
        listName: String,
        payload: Array,
    },
    data() {
        const { listName } = this
        return {
            modal: false,
            tags: (listName === 'need') ? {
                satellite_name: '衛星名稱',
                weight_kg: '重量(kg)',
                eta_height_km: '高度',
                inclination: '傾角(度)',
                arrival_date: '發射日期',
            } : {
                mission_arrival_deadline: '發射日期',
                limit_weight: '限制重量(kg)',
                seat_price: '價格(百萬)',
            },
            contactTags: {
                phone: '電話',
                email: '信箱',
                name: '聯絡',
            },
            detailTags : {
                launch_rocket: '名稱',
                rocket_max_payload_weight: '最大載重',
                target_height_km: '高度',
                target_inclination: '傾角',
            },
            itemInfo: null,
            detail: null,
        }
    },
    methods: {
        getContact: function(payload) {
            switch(this.listName) {
                case 'need':
                    api.getClientById(payload.request_by,this.getContactOnSuccess,this.onFailed);
                    break;
                case 'sale':
                    api.getMission(payload.mission_id,this.getDetailOnSuccess,this.onFailed);
                    break;
            }
        },
        getDetailOnSuccess: function(data) {
            this.detail = data;
            api.getClientById(this.detail.create_by,this.getContactOnSuccess,this.onFailed);
        },
        getContactOnSuccess: function(data) {
            this.itemInfo = data;
            if(this.itemInfo) {
                this.modal = true;
            }
        },
        onFailed: function() {
            this.$message({
                type: 'error',
                message: 'data not found',
                center: true,
            })
        }
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
    right: 0px;
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
    right: -150px;
    width: 100px;
    height: 100%;
    border-left: 1px solid #fff;
    transition: right 1s;
}
.buttonWrapper:hover {
    background-color: rgba(255,255,255,0.3);
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
.noData {
    width: 100%;
    height: 100%;
}
.modal {
    flex-direction: column;
    position: relative;
    background-color: rgba(0,0,0,0.3);
    width: 100%;
    height: 255px;
    transition: opacity .5s;
}
.createModal {
    opacity: 1;
}
.cross {
    top: 20px;
  right: 20px;
}
.itemInfoRow {
    display: flex;
}
</style>