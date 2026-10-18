export const terminal = status => ['done', 'failed', 'cancelled'].includes(status);
export function parentPath(path) {
  const index = Math.max(path.lastIndexOf('/'), path.lastIndexOf('\\'));
  if (index < 0) throw new Error('An absolute source path is required');
  if (index === 0 || (index === 2 && path[1] === ':')) return path.slice(0, index + 1);
  return path.slice(0, index);
}
export function matchingFiles(files, format, onlyPath = null) {
  return files.filter(file => (!onlyPath || file.path === onlyPath) && file.formats.some(f => f.id === format && f.available));
}
export function mergeJob(jobs, job) {
  const old = jobs.find(j => j.id === job.id);
  // A command response can arrive after the worker's terminal event.
  if (old && (terminal(old.status) || (old.status === 'running' && job.status === 'queued'))) return jobs;
  return old ? jobs.map(j => j.id === job.id ? job : j) : [...jobs, job];
}
export function sizeLabel(bytes) {
  return bytes >= 1048576 ? `${(bytes / 1048576).toFixed(1)} MB` : `${Math.max(1, Math.round(bytes / 1024))} KB`;
}

