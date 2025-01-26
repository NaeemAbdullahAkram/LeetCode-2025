var maximumInvitations = function(favorite) {
    return Math.max(findLargestCycle(favorite), calculateLongestPath(favorite));
};

/**
 * Finds the largest cycle in the graph.
 * @param {number[]} favorites - Array representing the favorite colleague of each employee.
 * @returns {number} - The size of the largest cycle.
 */
function findLargestCycle(favorites) {
    const n = favorites.length;
    const visited = Array(n).fill(false); // Track which nodes are visited
    let largestCycle = 0;

    // Iterate over all nodes
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            const cycleNodes = [];
            let currentNode = i;

            // Traverse the cycle starting from this node
            while (!visited[currentNode]) {
                cycleNodes.push(currentNode);
                visited[currentNode] = true;
                currentNode = favorites[currentNode];
            }

            // Calculate the length of the cycle
            for (let j = 0; j < cycleNodes.length; j++) {
                if (cycleNodes[j] === currentNode) {
                    largestCycle = Math.max(largestCycle, cycleNodes.length - j);
                }
            }
        }
    }
    return largestCycle; // Return the largest cycle length
}

/**
 * Calculates the longest path to mutual pairs and returns their total length.
 * @param {number[]} favorites - Array representing the favorite colleague of each employee.
 * @returns {number} - The total length of all paths leading to mutual pairs.
 */
function calculateLongestPath(favorites) {
    const n = favorites.length;
    const inDegree = Array(n).fill(0); // Track in-degree (number of incoming edges)
    const longestPath = Array(n).fill(1); // Track the longest path from each node
    const queue = [];

    // Calculate the in-degree for each node
    for (const favorite of favorites) {
        inDegree[favorite]++;
    }

    // Enqueue all nodes with no incoming edges
    for (let i = 0; i < n; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }

    let totalInvitations = 0;

    // Perform topological sorting to find the longest paths
    while (queue.length) {
        const currentNode = queue.pop();
        longestPath[favorites[currentNode]] = Math.max(longestPath[favorites[currentNode]], longestPath[currentNode] + 1);

        // Decrease in-degree and enqueue if any node has no more incoming edges
        if (--inDegree[favorites[currentNode]] === 0) {
            queue.push(favorites[currentNode]);
        }
    }

    // For every node that points to itself, add the longest path value to total invitations
    for (let i = 0; i < n; i++) {
        if (i === favorites[favorites[i]]) {
            totalInvitations += longestPath[i];
        }
    }

    return totalInvitations;
}