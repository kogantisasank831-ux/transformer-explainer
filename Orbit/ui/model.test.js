import test from 'node:test';
import assert from 'node:assert/strict';
import { parentPath, matchingFiles, mergeJob } from './model.js';
test('output directory handles Windows and Unix root paths', () => {
  assert.equal(parentPath('C:\\photo.png'), 'C:\\');
  assert.equal(parentPath('C:\\Users\\User\\photo.png'), 'C:\\Users\\User');
  assert.equal(parentPath('/photo.png'), '/');
  assert.equal(parentPath('/Users/user/photo.png'), '/Users/user');
});
test('batch excludes unsupported and unavailable formats explicitly', () => {
  const files = [{path:'a',formats:[{id:'pdf',available:true}]}, {path:'b',formats:[{id:'pdf',available:false}]}, {path:'c',formats:[{id:'png',available:true}]}];
  assert.deepEqual(matchingFiles(files,'pdf').map(f=>f.path),['a']);
  assert.equal(matchingFiles(files,'pdf','c').length,0);
});
test('late enqueue response cannot roll back a completed or running job', () => {
  assert.equal(mergeJob([{id:'1',status:'done'}],{id:'1',status:'queued'})[0].status,'done');
  assert.equal(mergeJob([{id:'1',status:'running'}],{id:'1',status:'queued'})[0].status,'running');
});

