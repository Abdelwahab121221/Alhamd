import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import Header from '../components/Header'
function StudentPage() {
  const { student } = useParams()
  const [tables, setTables] = useState([])
  const [weeks, setWeeks] = useState(1)
  let days = ['saturday', 'sunday', 'monday', 'tuesday', 'Wednesday', 'thursday']
  useEffect(() => {
    setTables([...tables,
      <>
    <table>
      <thead>
        <tr>
          <th>day</th>
          <th>date</th>
          <th>is here</th>
          <th>num of pages</th>
          <th>al sayra</th>
          <th>from to</th>
        </tr>
      </thead>
      <tbody>
        {days.map((day) => {
          return (
            <tr>
              <td>{day}</td>
              <td><input type="datetime-local" /></td>
              <td><input type="checkbox" /></td>
              <td><input type="number" /></td>
              <td><textarea ></textarea></td>
              <td><textarea></textarea></td>
            </tr>
          )
        })}
      </tbody>
    </table>
    <hr />
    </>
    ])
  }, [weeks])
  return (
    <div className='studentPage'>
      <Header lies={[]} />
      <div className="content">
        <h1>{student}</h1>
        <div className="tables">
          {tables}
        </div>
        <button onClick={() => {
          setWeeks(weeks + 1)
        }}>add</button>
      </div >
    </div>
  )
}

export default StudentPage