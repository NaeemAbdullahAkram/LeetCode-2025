const findRedundantConnection = (edges) => {
    const u = {};
    const find = a => !u[a] || u[a] === a ? u[a] = a : find(u[a]);
    for (let [a, b] of edges){
        if (find(a) - find(b)) {
            u[find(a)] = u[find(b)];
        } else {
            return [a, b];
        }
    }
};