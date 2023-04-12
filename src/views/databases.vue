<template>
    <!-- eslint-disable -->
    <div>
      <el-popover
        placement="bottom"
        title="New Employee"
        width="200"
        trigger="click"
      >
        <el-input
          placeholder="John Doe"
          v-model="name"
          @blur="createEmployee(name, date)"
        ></el-input>
        <el-button round slot="reference" type="success"
          >Add New Employee</el-button
        >
      </el-popover>
      <el-table
        :data="
          employeesData.filter(
            (data) =>
              !search || data.name.toLowerCase().includes(search.toLowerCase())
          )
        "
        style="width: 100%;"
      >
        <el-table-column label="Date" prop="date"> </el-table-column>
        <el-table-column label="Name" prop="name"> </el-table-column>
        <el-table-column align="right">
          <template slot="header" :slot-scope="scope">
            <el-input v-model="search" size="mini" placeholder="Type to search" />
          </template>
          <template slot-scope="scope">
            <el-popover
              placement="bottom"
              title="Edit Employee"
              width="200"
              trigger="click"
            >
              <el-input
                placeholder="John Doe"
                v-model="scope.row.name"
                @blur="updateEmployee(scope.row.id, scope.row.name, date)"
              ></el-input>
              <el-button size="mini" slot="reference">Edit</el-button>
            </el-popover>
            <el-button
              size="mini"
              type="danger"
              @click="deleteEmployee(scope.row.id)"
              >Delete</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>
  </template>
  
  <script>
  
  export default {
    name: 'app',
    data(){
      return {
        name: '',
        employeesData: []
      }
    }
  }
  </script>