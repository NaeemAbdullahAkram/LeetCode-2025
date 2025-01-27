const checkIfPrerequisite = (numCourses, prerequisites, queries) => {
    const isReachable = Array(numCourses).fill().map(_ => Array(numCourses).fill(false));
    prerequisites.forEach(([u, v]) => isReachable[u][v] = true);
    for (let i = 0; i < numCourses; i++) {
        for (let j = 0; j < numCourses; j++) {
            for (let k = 0; k < numCourses; k++) {
                if (isReachable[j][i] && isReachable[i][k]) {
                    isReachable[j][k] = true;
                }
            }
        }
    }
    return queries.map(([u, v]) => isReachable[u][v]);
};