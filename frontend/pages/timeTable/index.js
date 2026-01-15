import './style.css';

export default function Home() {
  return (
    <div class="app">
        <aside class="sidebar">
            <div class="logo">EduManage</div>

            <nav class="menu">
            <a>Dashboard</a>
            <a>Students</a>
            <a>Staff</a>
            <a class="active">Timetable</a>
            <a>Exams</a>
            </nav>

            <div class="sidebar-footer">
            <small>Alex Morgan</small>
            <span>Admin</span>
            </div>
        </aside>

        <main class="main">

            <header class="header">
            <div>
                <h1>Timetable Management</h1>
                <p>Class Schedule · Grade 10A · Term 1, 2024</p>
            </div>

            <div class="actions">
                <button class="btn outline">Export</button>
                <button class="btn primary">Save Changes</button>
            </div>
            </header>

            <section class="filters">
            <select>
                <option>Grade 10A</option>
            </select>

            <div class="chips">
                <span class="chip active">All Subjects</span>
                <span class="chip">Science Dept</span>
                <span class="chip">Math Dept</span>
                <span class="chip">Humanities</span>
            </div>
            </section>

            <div class="content">

            <section class="timetable">

                <div class="grid-header">
                <span></span>
                <span>Monday</span>
                <span>Tuesday</span>
                <span>Wednesday</span>
                <span>Thursday</span>
                <span>Friday</span>
                </div>

                <div class="grid">

                <div class="time">08:00</div>
                <div class="grid_feild">
                    <div class="card blue">
                    <div class="slot_title"><h1>Mathematics</h1></div>
                    <div class="slot_assigned"><p>Mrs.Cruis Mensah</p></div>
                    <div class="slot_location">rom 101</div>
                    </div>
                </div>
                <div class="grid_feild"><div class="card green">Physics</div></div>
                <div class="grid_feild"><div class="card empty"><svg xmlns="http://www.w3.org/2000/svg" height="60px" viewBox="0 -960 960 960" width="60px" fill="#e3e3e3"><path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/></svg></div></div>
                <div class="grid_feild"><div class="card blue">Mathematics</div></div>
                <div class="grid_feild"><div class="card yellow">History</div></div>

                <div class="time">09:00</div>
                <div class="grid_feild"><div class="card purple">English Lit</div></div>
                <div class="grid_feild"><div class="card red">Chemistry</div></div>
                <div class="grid_feild"><div class="card green">Biology</div></div>
                <div class="grid_feild"><div class="card green">Physics</div></div>
                <div class="grid_feild"><div class="card empty"><svg xmlns="http://www.w3.org/2000/svg" height="60px" viewBox="0 -960 960 960" width="60px" fill="#e3e3e3"><path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/></svg></div></div>

                <div class="break">RECESS BREAK</div>

                <div class="time">10:30</div>
                <div class="grid_feild"><div class="card yellow">History</div></div>
                <div class="grid_feild"><div class="card conflict">Geography<br/><small>Conflict</small></div></div>
                <div class="grid_feild"><div class="card pink">Art & Design</div></div>
                <div class="grid_feild"><div class="card empty"><h1>Free</h1></div></div>
                <div class="grid_feild"><div class="card red">Chemistry</div></div>

                <div class="time">11:30</div>
                <div class="grid_feild"><div class="card orange">PE</div></div>
                <div class="grid_feild"><div class="card yellow">History</div></div>
                <div class="grid_feild"><div class="card purple">English Lit</div></div>
                <div class="grid_feild"><div class="card cyan">Geography</div></div>
                <div class="grid_feild"><div class="card blue">Mathematics</div></div>

                </div>
            </section>
            <aside class="unscheduled">
                <h3>Unscheduled</h3>
                <input placeholder="Search subjects..." />

                <div class="list">
                <div class="item">Calculus II</div>
                <div class="item">Geometry</div>
                <div class="item">Physics Lab</div>
                <div class="item">Biology Intro</div>
                </div>

                <p class="hint">
                Drag items onto the grid to schedule them.
                </p>
            </aside>

            </div>

        </main>
    </div>
  );
}

